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
from core.navigation import Router
from services.authentication_service import AuthenticationService
from shared.components import LoginForm
from shared.components import Sidebar
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
    """

    load_css()

    initialize_database()


def render_application() -> None:
    """
    Render authenticated application.
    """

    sidebar = Sidebar()

    selected_route = sidebar.render()

    Router.navigate(selected_route)


def main() -> None:
    """
    Application entry point.
    """

    configure_application()

    initialize_application()

    auth = AuthenticationService()

    if not auth.is_authenticated():

        login = LoginForm()

        login.render()

        return

    render_application()


if __name__ == "__main__":
    main()