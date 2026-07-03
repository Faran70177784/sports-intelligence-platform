"""
Sports Intelligence Platform

File: page.py
Author: Syed Faran Ali

Description:
Dashboard module for the Sports Intelligence Platform.
Displays executive KPIs and recent activity.
"""

import streamlit as st

from shared.layouts import AppLayout


def render() -> None:
    """
    Render the Dashboard page.
    """

    # ------------------------------------------------------------------
    # Page Layout
    # ------------------------------------------------------------------

    AppLayout.begin(
        title="Dashboard",
        subtitle="Executive overview of the Sports Intelligence Platform."
    )

    # ------------------------------------------------------------------
    # Key Performance Indicators
    # ------------------------------------------------------------------

    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Sports",
            value="5",
            delta=None
        )

    with col2:
        st.metric(
            label="Organizations",
            value="0",
            delta=None
        )

    with col3:
        st.metric(
            label="Matches",
            value="0",
            delta=None
        )

    with col4:
        st.metric(
            label="Reports",
            value="0",
            delta=None
        )

    st.divider()

    # ------------------------------------------------------------------
    # Recent Activity
    # ------------------------------------------------------------------

    st.subheader("Recent Activity")

    st.info(
        "No activity available.\n\n"
        "Import sports data to begin using the platform."
    )

    st.divider()

    # ------------------------------------------------------------------
    # Quick Actions
    # ------------------------------------------------------------------

    st.subheader("Quick Actions")

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

    # ------------------------------------------------------------------
    # System Information
    # ------------------------------------------------------------------

    st.divider()

    with st.expander("System Information", expanded=False):

        st.write("Application Version: 0.3.0")
        st.write("Platform: Sports Intelligence Platform")
        st.write("Environment: Development")
        st.write("Status: Operational")

    # ------------------------------------------------------------------
    # Footer Layout
    # ------------------------------------------------------------------

    AppLayout.end()