import os


class Settings:
    BASE_URL: str | None = os.getenv("BASE_URL")  # "https://api.casino-stage.com/api/v1/"
    USERNAME: str | None = os.getenv("USERNAME")  # "archangel"
    PASSWORD: str | None = os.getenv("PASSWORD")  # "Mike2025!"

