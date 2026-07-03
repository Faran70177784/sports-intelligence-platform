"""
Sports Intelligence Platform

File: section_title.py
Author: Syed Faran Ali

Description:
Reusable section title.
"""

import streamlit as st


class SectionTitle:
    """Reusable section title."""

    @staticmethod
    def render(title: str) -> None:
        """Render a section title."""

        st.subheader(title)