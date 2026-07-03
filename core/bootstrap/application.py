"""
Application Bootstrap
"""

from core.container import container
from core.container.providers import provide_configuration


class Application:

    def initialize(self):

        container.register(

            "config",

            provide_configuration()

        )

        print("Application initialized.")