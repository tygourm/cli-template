from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    VERSION: str = "0.0.2"

    model_config = SettingsConfigDict()


settings = Settings()
