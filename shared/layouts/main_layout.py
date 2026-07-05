"""
Sports Intelligence Platform

File: main_layout.py
Author: Syed Faran Ali

Description:
Main application layout.

Responsible for rendering the authenticated
application shell.
"""

from core.navigation import Router
from shared.components import Sidebar


class MainLayout:
    """Main application layout."""

    def render(self) -> None:
        """
        Render the authenticated application.
        """

        sidebar = Sidebar()

        selected_route = sidebar.render()

        Router.navigate(selected_route)