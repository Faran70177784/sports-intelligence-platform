"""
Service Registry

Stores application singleton services.
"""

from typing import Any


class ServiceRegistry:

    def __init__(self):

        self._services: dict[str, Any] = {}

    def register(
        self,
        name: str,
        service: Any
    ) -> None:

        self._services[name] = service

    def get(self, name: str):

        if name not in self._services:

            raise KeyError(
                f"Service '{name}' is not registered."
            )

        return self._services[name]

    def exists(self, name: str):

        return name in self._services