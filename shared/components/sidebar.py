"""
Sports Intelligence Platform

File: sidebar.py
Author: Syed Faran Ali

Description:
Reusable application sidebar.
"""

import streamlit as st

from services.authentication_service import AuthenticationService
from shared.components.logout_button import LogoutButton
from shared.components.menu import MENU
from shared.styles.theme import theme


class Sidebar:
    """Application sidebar."""

    def __init__(self) -> None:
        self.auth = AuthenticationService()

    def render(self) -> str:
        """Render the application sidebar."""

        st.sidebar.title(theme.APP_NAME)

        st.sidebar.caption(
            f"Version {theme.VERSION}"
        )

        st.sidebar.divider()

        user = self.auth.current_user()

        if user is not None:

            st.sidebar.markdown(
                "### 👤 Logged in as"
            )

            st.sidebar.markdown(
                f"**{user['username']}**"
            )

            st.sidebar.caption(
                user["role"]
            )

            LogoutButton().render()

            st.sidebar.divider()

        labels = [
            f"{item.icon}  {item.title}"
            for item in MENU
        ]

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

            if (
                f"{item.icon}  {item.title}"
                == selected
            ):
                return item.route

        return "dashboard"