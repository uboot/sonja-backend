from fastapi.testclient import TestClient

from public.config import api_prefix
from public.main import app
from public.test.api import ApiTestCase
from sonja.test.util import create_commit, create_ecosystem, create_profile, create_run, run_create_operation

client = TestClient(app)


class TestGeneral(ApiTestCase):
    def setUp(self):
        self.crawler_mock.reset_mock()
        self.redis_client_mock.reset_mock()

    def test_clear_ecosystems(self):
        run_create_operation(create_ecosystem, dict())
        response = client.post(f"{api_prefix}/clear_ecosystems", headers=self.admin_headers)
        self.assertEqual(200, response.status_code)

    def test_populate_database(self):
        run_create_operation(create_ecosystem, dict())
        response = client.post(f"{api_prefix}/populate_database", headers=self.admin_headers)
        self.assertEqual(200, response.status_code)

    def test_add_build(self):
        ecosystem_id = run_create_operation(create_ecosystem, dict())
        run_create_operation(create_profile, dict(), ecosystem_id)
        run_create_operation(create_commit, dict(), ecosystem_id)
        response = client.post(f"{api_prefix}/add_build", headers=self.admin_headers)
        self.assertEqual(200, response.status_code)
        self.redis_client_mock.publish_build_update.assert_called_once()

    def test_add_run(self):
        run_create_operation(create_ecosystem, dict())
        response = client.post(f"{api_prefix}/add_run", headers=self.admin_headers)
        self.assertEqual(200, response.status_code)
        self.redis_client_mock.publish_run_update.assert_called_once()

    def test_add_log_line(self):
        ecosystem_id = run_create_operation(create_ecosystem, dict())
        run_create_operation(create_run, dict(), ecosystem_id)
        response = client.post(f"{api_prefix}/add_log_line", headers=self.admin_headers)
        self.assertEqual(200, response.status_code)
        self.redis_client_mock.publish_log_line_update.assert_called_once()

    def test_process_repo(self):
        response = client.post(f"{api_prefix}/process_repo/1", headers=self.user_headers)
        self.assertEqual(200, response.status_code)
        self.crawler_mock.process_repo.assert_called_with("1")
