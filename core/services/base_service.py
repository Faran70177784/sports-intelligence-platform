"""
Base Service
Sports Intelligence Platform

Author:
    Syed Faran Ali

Description:
    Base class inherited by all application services.
"""

from abc import ABC


class BaseService(ABC):
    """
    Base class for every service.
    """

    @property
    def service_name(self) -> str:
        return self.__class__.__name__