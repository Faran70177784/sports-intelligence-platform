"""
Sports Intelligence Platform

File: app_layout.py
Author: Syed Faran Ali

Description:
Reusable application layout.
"""

from shared.layouts.content_container import ContentContainer
from shared.layouts.page_header import PageHeader
from shared.layouts.status_bar import StatusBar


class AppLayout:
    """Application layout."""

    @staticmethod
    def begin(
        title: str,
        subtitle: str
    ) -> None:

        PageHeader.render(
            title,
            subtitle
        )

        ContentContainer.begin()

    @staticmethod
    def end() -> None:

        ContentContainer.end()

        StatusBar.render()