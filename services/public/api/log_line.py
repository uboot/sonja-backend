from aioredis import Channel, Redis
from fastapi import APIRouter, Depends, HTTPException
from fastapi_plugins import depends_redis
from sse_starlette.sse import EventSourceResponse
from public.auth import get_read
from public.schemas.log_line import LogLineReadList, LogLineReadItem
from public.crud.log_line import read_log_lines, read_log_line
from sonja.database import get_session, Session, session_scope
from sonja.config import logger
from typing import Optional

router = APIRouter()


@router.get("/log_line", response_model=LogLineReadList, response_model_by_alias=False,
            dependencies=[Depends(get_read)])
def get_log_line_list(run_id: str, page: Optional[int] = None, per_page:  Optional[int] = None,
                      session: Session = Depends(get_session)):
    return LogLineReadList.from_db(**read_log_lines(session, run_id, page, per_page))


@router.get("/log_line/{log_line_id}", response_model=LogLineReadItem, response_model_by_alias=False,
            dependencies=[Depends(get_read)])
def get_log_line_item(log_line_id: str, session: Session = Depends(get_session)):
    build = read_log_line(session, log_line_id)
    if build is None:
        raise HTTPException(status_code=404, detail="Log line not found")
    return LogLineReadItem.from_db(build)


@router.get("/event/run/{run_id}/log_line", response_model=LogLineReadItem, response_model_by_alias=False)
async def get_line_events(run_id: str, redis: Redis = Depends(depends_redis)):
    return EventSourceResponse(subscribe(f"run:{run_id}", redis))


async def subscribe(channel: str, redis: Redis):
    (channel_subscription,) = await redis.subscribe(channel=Channel(channel, False))
    while await channel_subscription.wait_message():
        message = await channel_subscription.get_json()
        item_json = None
        with session_scope() as session:
            item_id = str(message["id"])
            item_type = message["type"]

            if item_type != "log_line":
                logger.warning("Did not send event for unsupported type '%s'", item_type)

            item = read_log_line(session, item_id)
            if item:
                item_json = LogLineReadItem.from_db(item).json()

        if item_json:
            logger.debug("Send log line event '%s' received on '%s'", item_json, channel)
            yield { "event": "update", "data": item_json }
        else:
            logger.warning("Could not read updated log line '%s'", item_id)
