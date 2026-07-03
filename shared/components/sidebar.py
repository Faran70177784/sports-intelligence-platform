"""
Sports Intelligence Platform

File: sidebar.py
Author: Syed Faran Ali

Description:
Reusable application sidebar.
"""

import streamlit as st

from shared.components.menu import MENU
from shared.styles.theme import theme


class Sidebar:
    """Application sidebar."""

    def render(self) -> str:
        """Render sidebar."""

        st.sidebar.title(theme.APP_NAME)

        st.sidebar.caption(
            f"Version {theme.VERSION}"
        )

        st.sidebar.divider()

        labels = [item.title for item in MENU]

        selected = st.sidebar.radio(

            label="Navigation",

            options=labels,

            label_visibility="collapsed",

        )

        st.sidebar.divider()

        st.sidebar.caption(
            "© 2026 Syed Faran Ali"
        )

        for item in MENU:

            if item.title == selected:

                return item.route

        return "dashboard"