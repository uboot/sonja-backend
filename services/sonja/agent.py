from datetime import datetime
from typing import List

from sonja.builder import Builder, BuildFailed
from sonja.config import connect_to_database, logger
from sonja.database import session_scope, get_current_configuration
from sonja.redis import RedisClient
from sonja.client import Scheduler
from sonja.manager import Manager
from sonja.model import BuildStatus, Build, Profile, Platform, Run, RunStatus, LogLine
from sonja.worker import Worker
from sqlalchemy.exc import OperationalError
import asyncio
import os
import time


sonja_os = os.environ.get("SONJA_AGENT_OS", "Linux")
TIMEOUT = 10


async def _run_build(builder):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, builder.pull_image)
    await loop.run_in_executor(None, builder.create_build_files)
    await loop.run_in_executor(None, builder.setup_container)
    await loop.run_in_executor(None, builder.run_build)


class Agent(Worker):
    def __init__(self, scheduler: Scheduler, redis_client: RedisClient):
        super().__init__()
        connect_to_database()
        self.__build_id = None
        self.__run_id = None
        self.__log_line_counter = None
        self.__scheduler = scheduler
        self.__redis_client = redis_client
        self.__manager = Manager(redis_client)

    async def work(self, payload):
        new_builds = True
        while new_builds:
            try:
                new_builds = await self.__process_builds()
            except Exception as e:
                logger.error("Processing builds failed: %s", e)
                logger.info("Retry in %i seconds", TIMEOUT)
                time.sleep(TIMEOUT)

    async def __process_builds(self):
        logger.info("Start processing builds")
        platform = Platform.linux if sonja_os == "Linux" else Platform.windows
        try:
            with session_scope() as session:
                configuration = get_current_configuration(session)
                build = session\
                    .query(Build)\
                    .join(Build.profile)\
                    .filter(Profile.platform == platform,\
                            Build.status == BuildStatus.new)\
                    .populate_existing()\
                    .with_for_update(skip_locked=True, of=Build)\
                    .first()

                if not build:
                    logger.info("Stop processing builds with *no* builds processed")
                    return False

                logger.info("Set status of build '%d' to 'active'", build.id)
                self.__build_id = build.id
                build.status = BuildStatus.active
                run = Run()
                run.build = build
                run.status = RunStatus.active
                run.started = datetime.utcnow()
                run.updated = datetime.utcnow()
                session.commit()
                self.__run_id = run.id
                self.__log_line_counter = 1
                self.__redis_client.publish_build_update(build)
                self.__redis_client.publish_run_update(run)

                container = build.profile.container
                ecosystem = build.profile.ecosystem
                profile = build.profile
                commit = build.commit
                channel = build.commit.channel
                repo = build.commit.repo
                parameters = {
                    "conan_config_url": ecosystem.conan_config_url,
                    "conan_config_path": ecosystem.conan_config_path,
                    "conan_config_branch": ecosystem.conan_config_branch,
                    "conan_remote": channel.conan_remote,
                    "conan_profile": profile.conan_profile,
                    "conan_options": " ".join(["-o {0}={1}".format(option.key, option.value)
                                               for option in commit.repo.options]),
                    "git_url": commit.repo.url,
                    "git_sha": commit.sha,
                    "git_credentials": [
                        {
                            "url": c.url,
                            "username": c.username,
                            "password": c.password
                        } for c in configuration.git_credentials
                    ],
                    "sonja_user": ecosystem.user,
                    "channel": channel.conan_channel,
                    "version": "" if not repo.version else repo.version,
                    "path": "./{0}/{1}".format(repo.path, "conanfile.py")
                            if repo.path != "" else "./conanfile.py",
                    "ssh_key": configuration.ssh_key,
                    "known_hosts": configuration.known_hosts,
                    "docker_credentials": [
                        {
                            "server": c.server,
                            "username": c.username,
                            "password": c.password
                        } for c in configuration.docker_credentials
                    ],
                    "conan_credentials": [
                        {
                            "remote": c.remote,
                            "username": c.username,
                            "password": c.password
                        } for c in ecosystem.conan_credentials
                    ],
                    "mtu": os.environ.get("SONJA_MTU", "1500")
                }
        except OperationalError as e:
            logger.error("Failed to access database: %s", e)
            logger.info("Try to reconnect in %i seconds", TIMEOUT)
            time.sleep(TIMEOUT)
            return True

        try:
            with Builder(sonja_os, container, parameters) as builder:
                try:
                    builder_task = asyncio.create_task(_run_build(builder))
                    while True:
                        # wait 10 seconds
                        done, _ = await asyncio.wait({builder_task}, timeout=10)
                        log_lines = [line for line in builder.get_log_lines()]
                        self.__append_to_logs(log_lines)
                        self.__update_run()

                        # if finished exit
                        if done:
                            builder_task.result()
                            break

                        # check if the build was stopped and cancel it
                        # if necessary
                        if self.__cancel_stopping_build(builder):
                            return True

                    logger.info("Process build output")
                    result = self.__manager.process_success(self.__build_id, builder.build_output)
                    if result.get("new_builds", False):
                        self.__trigger_scheduler()

                    self.__set_build_status(BuildStatus.success, RunStatus.success)
                except BuildFailed as e:
                    logger.info("Build '%d' failed", self.__build_id)
                    logger.info("%s", e)
                    self.__append_to_logs([str(e)])
                    self.__manager.process_failure(self.__build_id, builder.build_output)
                    self.__set_build_status(BuildStatus.error, RunStatus.error)
        except asyncio.CancelledError:
            logger.info("Agent was cancelled")
            self.__set_build_status(BuildStatus.new, RunStatus.stopped)
            raise
        except Exception as e:
            logger.error("Unexpected error while building: ", e)
            self.__set_build_status(BuildStatus.new, RunStatus.error)
        finally:
            self.__build_id = None
            self.__run_id = None
            self.__log_line_counter = None
            
        return True

    def __set_build_status(self, status: BuildStatus, run_status: RunStatus):
        logger.info("Set status of build '%d' to '%s'", self.__build_id, status)

        if not self.__build_id:
            return

        try:
            with session_scope() as session:
                run = session.query(Run) \
                    .filter_by(id=self.__run_id) \
                    .first()
                if run and run.build:
                    logger.info("Set status of run '%d' to '%s'", run.id , run_status)
                    run.status = run_status
                    run.build.status = status
                    session.commit()
                    self.__redis_client.publish_build_update(run.build)
                    self.__redis_client.publish_run_update(run)
                else:
                    logger.error("Failed to find run '%d' and/or its build in database", self.__run_id)
        except OperationalError as e:
            logger.error("Failed to set build status: %s", e)

    def __update_run(self):
        try:
            with session_scope() as session:
                run = session.query(Run) \
                    .filter_by(id=self.__run_id) \
                    .first()
                if run and run.build:
                    logger.debug("Update run '%d' to '%s'", run.id)
                    run.updated = datetime.utcnow()
                    session.commit()
                else:
                    logger.error("Failed to find run '%d' and/or its build in database", self.__run_id)
        except OperationalError as e:
            logger.error("Failed to update run: %s", e)

    def __append_to_logs(self, log_lines: List[str]):
        try:
            with session_scope() as session:
                for line in log_lines:
                    log_line = LogLine()
                    log_line.content = line.encode("cp1252", errors="replace")
                    log_line.time = datetime.utcnow()
                    log_line.run_id = self.__run_id
                    log_line.number = self.__log_line_counter
                    self.__log_line_counter += 1
                    session.add(log_line)
                    session.commit()
                    self.__redis_client.publish_log_line_update(log_line)
        except OperationalError as e:
            logger.error("Failed to update logs: %s", e)

    def __cancel_stopping_build(self, builder) -> bool:
        try:
            with session_scope() as session:
                build = session.query(Build) \
                    .filter_by(id=self.__build_id, status=BuildStatus.stopping) \
                    .first()
                if not build:
                    return False

                run = session.query(Run) \
                    .filter_by(id=self.__run_id) \
                    .first()

                logger.info("Cancel build '%d'", self.__build_id)
                builder.cancel()
                logger.info("Set status of build '%d' to 'stopped'", self.__build_id)
                build.status = BuildStatus.stopped
                run.status = RunStatus.stopped
                session.commit()
                self.__redis_client.publish_build_update(build)
                self.__redis_client.publish_run_update(run)
                self.__build_id = None
                return True
        except OperationalError as e:
            logger.error("Failed query and stop cancelled builds: %s", e)
            return False

    def __trigger_scheduler(self):
        logger.info('Trigger scheduler: process commits')
        if not self.__scheduler.process_commits():
            logger.error("Failed to trigger scheduler")
