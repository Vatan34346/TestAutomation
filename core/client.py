import httpx
from httpx import Response


class APIClient:
    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url
        self.client = httpx.Client(base_url=base_url)

    def post(self, url: str, json: dict | None = None) -> Response:
        return self.client.post(url, json=json)

    def get(self, url: str) -> Response:
        return self.client.get(url)

    def close(self) -> None:
        self.client.close()
