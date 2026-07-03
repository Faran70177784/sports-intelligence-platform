"""
Sports Intelligence Platform

File: menu.py
Author: Syed Faran Ali

Description:
Application navigation menu.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MenuItem:
    """Represents a sidebar menu item."""

    title: str
    icon: str
    route: str


MENU = [

    MenuItem("Dashboard", "📊", "dashboard"),

    MenuItem("Analytics", "📈", "analytics"),

    MenuItem("AI Intelligence", "🤖", "ai"),

    MenuItem("Data Import", "📥", "data_import"),

    MenuItem("Reports", "📄", "reports"),

    MenuItem("Organizations", "🏢", "organizations"),

    MenuItem("Administration", "🛠", "administration"),

    MenuItem("Settings", "⚙", "settings"),

]