from typing import Annotated, Optional, Final

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings): 
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8"
    )

    DATABASE_URL: Annotated[Final[str], Field(description="Url to database")]


settings = Settings()  # type: ignore
