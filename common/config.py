import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field


class Settings(BaseModel):
    model: str = Field(default="gemini-3.7-flash", alias="DEFAULT_MODEL")
    google_api_key: str | None = Field(default=None, alias="GOOGLE_API_KEY")
    use_vertexai: bool = Field(default=False, alias="GOOGLE_GENAI_USE_VERTEXAI")
    project: str | None = Field(default=None, alias="GOOGLE_CLOUD_PROJECT")
    location: str = Field(default="us-central1", alias="GOOGLE_CLOUD_LOCATION")
    gemini_cli_bin: str = Field(default="gemini", alias="GEMINI_CLI_BIN")
    gemini_cli_timeout: int = Field(default=120, alias="GEMINI_CLI_TIMEOUT_SECONDS")
    commerce_data_file: Path = Field(default=Path("data/products.json"), alias="COMMERCE_DATA_FILE")
    bug_workspace: Path = Field(default=Path("workspace/bug-assistant"), alias="BUG_WORKSPACE")

    model_config = {"populate_by_name": True, "extra": "ignore"}


@lru_cache
def settings() -> Settings:
    load_dotenv()
    aliases = {
        field.alias or name: os.getenv(field.alias or name)
        for name, field in Settings.model_fields.items()
    }
    values = {key: value for key, value in aliases.items() if value is not None}
    return Settings.model_validate(values)
