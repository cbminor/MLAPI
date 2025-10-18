from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "v1"
    MODEL_DIR: str = "app/models"

settings = Settings()
