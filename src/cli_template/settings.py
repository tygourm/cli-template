from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    version: str = "1.0.0"
    logs_filename: str = "cli-template.log"
    logs_format: str = "%(asctime)s [%(name)s] %(levelname)s %(message)s"
    logs_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    model_config = SettingsConfigDict()


settings = Settings()
