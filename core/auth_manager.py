from api.auth_api import AuthAPI, APIClient, Response


class AuthManager:
    def __init__(self, client: APIClient, username: str, password: str) -> None:
        self.client: APIClient = client
        self.username: str = username
        self.password: str = password
        self.auth_api: AuthAPI = AuthAPI(self.client)

    def authenticate(self) -> None:
        response: Response = self.auth_api.login(self.username, self.password)

        assert response.status_code == 200, f"Login failed: {response.status_code}"

        cookies = self.client.client.cookies

        assert "token" in cookies, "Access token cookie missing"
        assert "refresh_token" in cookies, "Refresh token cookie missing"
