"""
Sports Intelligence Platform

File: activity_card.py
Author: Syed Faran Ali

Description:
Recent activity component.
"""

import streamlit as st


class ActivityCard:
    """Reusable activity card."""

    @staticmethod
    def render(message: str) -> None:
        """Render activity information."""

        st.info(message)