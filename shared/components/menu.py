"""
Sports Intelligence Platform

File: menu.py
Author: Syed Faran Ali

Description:
Application navigation menu configuration.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MenuItem:
    """Navigation menu item."""

    title: str
    route: str
    icon: str


MENU = [
    MenuItem(
        title="Dashboard",
        route="dashboard",
        icon="🏠",
    ),
    MenuItem(
        title="Organizations",
        route="organizations",
        icon="🏢",
    ),
    MenuItem(
        title="Teams",
        route="teams",
        icon="👥",
    ),
    MenuItem(
        title="Players",
        route="players",
        icon="🏃",
    ),
    MenuItem(
        title="Matches",
        route="matches",
        icon="⚽",
    ),
    MenuItem(
        title="Events",
        route="events",
        icon="📋",
    ),
]