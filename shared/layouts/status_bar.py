"""
Sports Intelligence Platform

File: status_bar.py
Author: Syed Faran Ali

Description:
Application status bar.
"""

import streamlit as st


class StatusBar:
    """Bottom application status bar."""

    @staticmethod
    def render() -> None:
        """Render status bar."""

        st.divider()

        col1, col2 = st.columns([4, 1])

        with col1:
            st.caption(
                "Sports Intelligence Platform"
            )

        with col2:
            st.caption("v0.3.0")