"""
Sports Intelligence Platform
Configuration Manager

Author:
    Syed Faran Ali
"""

from pathlib import Path
from typing import Any

import yaml


class ConfigManager:
    """
    Central configuration loader.

    Loads YAML configuration files and provides
    a simple interface for retrieving values.
    """

    def __init__(self, config_directory: str = "config") -> None:
        self.config_directory = Path(config_directory)
        self._cache: dict[str, dict[str, Any]] = {}

    def load(self, filename: str) -> dict[str, Any]:
        """
        Load a YAML configuration file.
        """
        if filename in self._cache:
            return self._cache[filename]

        file_path = self.config_directory / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {file_path}"
            )

        with file_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file) or {}

        self._cache[filename] = config
        return config

    def get(self, filename: str, *keys: str, default: Any = None) -> Any:
        """
        Retrieve nested configuration values.

        Example:
            get("app.yaml", "application", "name")
        """
        data = self.load(filename)

        for key in keys:
            if not isinstance(data, dict):
                return default
            data = data.get(key)

        return default if data is None else data