"""
Sports Intelligence Platform

File: content_container.py
Author: Syed Faran Ali

Description:
Reusable content container.
"""

import streamlit as st


class ContentContainer:
    """Main page content container."""

    @staticmethod
    def begin() -> None:
        """Begin page container."""

        st.container()

    @staticmethod
    def end() -> None:
        """End page container."""

        pass