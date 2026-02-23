import os


class Settings:
    BASE_URL: str | None = os.getenv("BASE_URL")  # "https://api.casino-stage.com/api/v1/"
    USERNAME: str | None = "archangel"  # os.getenv("TEST_USERNAME", "testuser")
    PASSWORD: str | None = "Mike2025!"  # os.getenv("TEST_PASSWORD", "password")

