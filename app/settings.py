from typing import Any

import toml  # type: ignore
from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):

    _pyproject: dict[str, Any] = toml.load("pyproject.toml")

    name: str = _pyproject["tool"]["poetry"]["name"]
    version: str = _pyproject["tool"]["poetry"]["version"]


project_settings = ProjectSettings()
