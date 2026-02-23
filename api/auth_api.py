from httpx import Response
from core.client import APIClient


class AuthAPI:
    def __init__(self, client: APIClient) -> None:
        self.client: APIClient = client

    def login(self, username: str, password: str) -> Response:
        return self.client.post(
            "admin/auth/login",
            json={"login": username, "pass": password, "ip": "84.32.34.51",
                  "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
                  "domain": "admin.casino-stage.com"})

    def refresh(self) -> Response:
        return self.client.post("admin/auth/refresh-token")
