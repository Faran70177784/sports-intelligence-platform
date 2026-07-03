"""
Sports Intelligence Platform

File: page_header.py
Author: Syed Faran Ali

Description:
Reusable page header component.
"""

import streamlit as st


class PageHeader:
    """Reusable page header."""

    @staticmethod
    def render(
        title: str,
        subtitle: str = ""
    ) -> None:
        """Render the page header."""

        st.title(title)

        if subtitle:
            st.caption(subtitle)

        st.divider()