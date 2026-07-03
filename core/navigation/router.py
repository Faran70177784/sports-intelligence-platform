"""
Sports Intelligence Platform

File: router.py
Author: Syed Faran Ali

Description:
Application router.
"""

import streamlit as st

from core.navigation.loader import ModuleLoader


class Router:
    """Application router."""

    @staticmethod
    def navigate(module_name: str) -> None:
        """Navigate to a module."""

        try:
            module = ModuleLoader.load(module_name)

            module.render()

        except ModuleNotFoundError:

            st.error(
                f"Module '{module_name}' not found."
            )