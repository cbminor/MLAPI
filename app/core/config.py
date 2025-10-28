import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "v1"
    MODEL_DIR: str = "app/models"
    DO_SPACE_REGION: str = os.getenv("DO_SPACE_REGION", "nyc3")
    DO_SPACE_NAME: str = os.getenv("DO_SPACE_NAME", "your-space-name")
    DO_SPACE_ENDPOINT: str = os.getenv("DO_SPACE_ENDPOINT", "https://nyc3.digitaloceanspaces.com")
    DO_SPACE_ACCESS_KEY: str = os.getenv("DO_SPACE_ACCESS_KEY", "your-access-key")
    DO_SPACE_SECRET_KEY: str = os.getenv("DO_SPACE_SECRET_KEY", "your-secret-key")

    class Config:
        env_file = ".env"

settings = Settings()
