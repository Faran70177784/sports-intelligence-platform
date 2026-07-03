"""
Header component.
"""

import streamlit as st


def render():
    """
    Render header.
    """

    st.set_page_config(
        page_title="Sports Analytics Dashboard Platform",
        page_icon="🏆",
        layout="wide",
        initial_sidebar_state="expanded",
    )