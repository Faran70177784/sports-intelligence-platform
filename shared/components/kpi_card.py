"""
Sports Intelligence Platform

File: kpi_card.py
Author: Syed Faran Ali

Description:
Reusable KPI card component.
"""

import streamlit as st


class KPICard:
    """Reusable KPI card."""

    @staticmethod
    def render(
        title: str,
        value: str,
        delta: str | None = None
    ) -> None:
        """
        Render a KPI card.

        Args:
            title: KPI title.
            value: KPI value.
            delta: Optional trend value.
        """

        st.metric(
            label=title,
            value=value,
            delta=delta
        )