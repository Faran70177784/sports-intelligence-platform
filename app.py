"""
Sports Intelligence Platform

File: app.py
Author: Syed Faran Ali

Description:
Main application entry point.
Initializes the Streamlit application,
loads the global theme,
renders the sidebar,
and routes the user to the selected module.
"""

import streamlit as st

from core.navigation import Router
from shared.components import Sidebar
from shared.styles import load_css
from core.database import initialize_database


def configure_application() -> None:
    """
    Configure global Streamlit settings.
    """

    st.set_page_config(
        page_title="Sports Intelligence Platform",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="expanded",
    )


def initialize_application() -> None:
    """
    Initialize application resources.
    """

    load_css()


    initialize_database()

def main() -> None:
    """
    Application entry point.
    """

    configure_application()

    initialize_application()

    sidebar = Sidebar()

    selected_route = sidebar.render()

    Router.navigate(selected_route)


if __name__ == "__main__":
    main()