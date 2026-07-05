"""
Sports Intelligence Platform

File: app.py
Author: Syed Faran Ali

Description:
Main application entry point.

Configures the Streamlit application,
initializes resources,
handles authentication,
and renders the dashboard.
"""

import streamlit as st

from core.database import initialize_database
from services.authentication_service import AuthenticationService
from shared.components import LoginForm
from shared.layouts import MainLayout
from shared.styles import load_css


def configure_application() -> None:
    """
    Configure global Streamlit settings.
    """

    st.set_page_config(
        page_title="Sports Intelligence Platform",
        page_icon="🏆",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def initialize_application() -> None:
    """
    Initialize application resources.

    This runs only once per Streamlit session.
    """

    load_css()

    if "app_initialized" not in st.session_state:

        initialize_database()

        st.session_state["app_initialized"] = True


def render_application() -> None:
    """
    Render authenticated application.
    """

    MainLayout().render()


def main() -> None:
    """
    Application entry point.
    """

    configure_application()

    initialize_application()

    auth = AuthenticationService()

    if not auth.is_authenticated():

        LoginForm().render()

        return

    render_application()


if __name__ == "__main__":
    main()