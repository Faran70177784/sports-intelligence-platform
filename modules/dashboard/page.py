"""
Sports Intelligence Platform

File: page.py
Author: Syed Faran Ali

Description:
Dashboard module for the Sports Intelligence Platform.
Displays executive KPIs, recent activity, quick actions,
and system information.
"""

import streamlit as st

from shared.components import (
    ActivityCard,
    KPICard,
    SectionTitle,
)
from shared.layouts import AppLayout


def render() -> None:
    """
    Render the Dashboard page.
    """

    # ---------------------------------------------------------
    # Page Layout
    # ---------------------------------------------------------

    AppLayout.begin(
        title="Dashboard",
        subtitle="Executive overview of the Sports Intelligence Platform."
    )

    # ---------------------------------------------------------
    # Key Performance Indicators
    # ---------------------------------------------------------

    SectionTitle.render("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        KPICard.render(
            title="Sports",
            value="5"
        )

    with col2:
        KPICard.render(
            title="Organizations",
            value="0"
        )

    with col3:
        KPICard.render(
            title="Matches",
            value="0"
        )

    with col4:
        KPICard.render(
            title="Reports",
            value="0"
        )

    st.divider()

    # ---------------------------------------------------------
    # Recent Activity
    # ---------------------------------------------------------

    SectionTitle.render("Recent Activity")

    ActivityCard.render(
        "No activity available. Import sports data to begin using the platform."
    )

    st.divider()

    # ---------------------------------------------------------
    # Quick Actions
    # ---------------------------------------------------------

    SectionTitle.render("Quick Actions")

    action_col1, action_col2, action_col3 = st.columns(3)

    with action_col1:
        st.button(
            "Import Data",
            use_container_width=True
        )

    with action_col2:
        st.button(
            "Open Analytics",
            use_container_width=True
        )

    with action_col3:
        st.button(
            "Generate Report",
            use_container_width=True
        )

    st.divider()

    # ---------------------------------------------------------
    # System Information
    # ---------------------------------------------------------

    with st.expander(
        "System Information",
        expanded=False
    ):
        st.write("Application Version: 0.3.0")
        st.write("Platform: Sports Intelligence Platform")
        st.write("Environment: Development")
        st.write("Status: Operational")

    # ---------------------------------------------------------
    # End Layout
    # ---------------------------------------------------------

    AppLayout.end()