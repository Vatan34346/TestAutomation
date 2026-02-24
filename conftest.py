import pytest
from core.client import APIClient
from core.auth_manager import AuthManager
from core.config import Settings


@pytest.fixture(scope="session")
def api_client():
    client: APIClient = APIClient(Settings.BASE_URL or "https://api.casino-stage.com/api/v1/")
    yield client
    client.close()


@pytest.fixture(scope="session")
def authentication_client(api_client: APIClient):
    manger: AuthManager = AuthManager(api_client, Settings.USERNAME, Settings.PASSWORD)
    manger.authenticate()
    return api_client
