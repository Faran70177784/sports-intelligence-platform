"""
Logout component.
"""

import streamlit as st

from services.authentication_service import AuthenticationService


class LogoutButton:

    def __init__(self):

        self.auth = AuthenticationService()

    def render(self) -> None:

        if st.sidebar.button(
            "🚪 Logout",
            use_container_width=True,
        ):

            self.auth.logout()

            st.rerun()