"""
Dependency Injection Container
"""

from core.container.registry import ServiceRegistry


class Container:

    def __init__(self):

        self.registry = ServiceRegistry()

    def register(
        self,
        name,
        service
    ):

        self.registry.register(
            name,
            service
        )

    def resolve(
        self,
        name
    ):

        return self.registry.get(name)