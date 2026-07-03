"""
Sports Intelligence Platform

File: routes.py
Author: Syed Faran Ali

Description:
Application route definitions.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    """Represents an application route."""

    title: str
    module: str


ROUTES: list[Route] = [
    Route("Dashboard", "dashboard"),
    Route("Analytics", "analytics"),
    Route("AI Intelligence", "ai"),
    Route("Data Import", "data_import"),
    Route("Reports", "reports"),
    Route("Organizations", "organizations"),
    Route("Administration", "administration"),
    Route("Settings", "settings"),
]