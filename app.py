"""
Sports Intelligence Platform

Application Entry Point
"""

import streamlit as st

from shared.styles import load_css
from shared.components import Sidebar


def main() -> None:
    """Start the application."""

    st.set_page_config(
        page_title="Sports Intelligence Platform",
        page_icon="🏆",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    load_css()

    sidebar = Sidebar()

    selected = sidebar.render()

    st.title("Sports Intelligence Platform")

    st.write(f"Current Module: **{selected}**")


if __name__ == "__main__":
    main()