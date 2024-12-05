from typing import Any

import toml
from pydantic_settings import BaseSettings, SettingsConfigDict


class _ProjectSettings(BaseSettings):
    _pyproject: dict[str, Any] = toml.load("./pyproject.toml")

    name: str = _pyproject["project"]["name"]
    version: str = _pyproject["project"]["version"]
    description: str = _pyproject["project"]["description"]

    model_config = SettingsConfigDict(frozen=True, toml_file="pyproject.toml")


project_settings: _ProjectSettings = _ProjectSettings()
