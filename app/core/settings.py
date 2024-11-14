from typing import Any

import toml  # type: ignore
from pydantic_settings import BaseSettings


class _ProjectSettings(BaseSettings):
    _pyproject: dict[str, Any] = toml.load("/app/pyproject.toml")

    name: str = _pyproject["project"]["name"]
    version: str = _pyproject["project"]["version"]


project_settings = _ProjectSettings()
