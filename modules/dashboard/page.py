"""
Sports Intelligence Platform

File: page.py
Author: Syed Faran Ali

Description:
Dashboard page.
"""

import streamlit as st


def render() -> None:
    """Render dashboard page."""

    st.title("Dashboard")

    st.write(
        "Welcome to the Sports Intelligence Platform."
    )