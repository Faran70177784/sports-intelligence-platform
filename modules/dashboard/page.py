"""
Sports Intelligence Platform

File: page.py
Author: Syed Faran Ali

Description:
Dashboard module for the Sports Intelligence Platform.
Displays executive KPIs, analytics, recent activity,
quick actions, and system information.
"""

import streamlit as st

from services.analytics_service import AnalyticsService
from shared.components import (
    ActivityCard,
    AnalyticsCharts,
    KPICard,
    SectionTitle,
)
from shared.layouts import AppLayout


analytics_service = AnalyticsService()


def render() -> None:
    """
    Render the Dashboard page.
    """

    AppLayout.begin(
        title="Dashboard",
        subtitle="Executive overview of the Sports Intelligence Platform.",
    )

    # ---------------------------------------------------------
    # Dashboard Statistics
    # ---------------------------------------------------------

    stats = analytics_service.dashboard_statistics()

    # ---------------------------------------------------------
    # Key Performance Indicators
    # ---------------------------------------------------------

    SectionTitle.render("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        KPICard.render(
            title="Organizations",
            value=stats["organizations"],
        )

    with col2:

        KPICard.render(
            title="Teams",
            value=stats["teams"],
        )

    with col3:

        KPICard.render(
            title="Players",
            value=stats["players"],
        )

    with col4:

        KPICard.render(
            title="Matches",
            value=stats["matches"],
        )

    st.divider()

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    SectionTitle.render("Analytics")

    event_data = analytics_service.event_distribution()
    team_data = analytics_service.players_per_team()

    left, right = st.columns(2)

    with left:

        AnalyticsCharts.pie_chart(
            event_data,
            title="Event Distribution",
        )

    with right:

        AnalyticsCharts.bar_chart(
            team_data,
            title="Players per Team",
            x_title="Team",
            y_title="Players",
        )

    st.divider()

    # ---------------------------------------------------------
    # Top Scorers
    # ---------------------------------------------------------

    SectionTitle.render("Top Scorers")

    scorers = analytics_service.top_scorers()

    if scorers:

        st.dataframe(
            {
                "Player": [player for player, _ in scorers],
                "Goals": [goals for _, goals in scorers],
            },
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.info(
            "No goals recorded."
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
            use_container_width=True,
        )

    with action_col2:

        st.button(
            "Open Analytics",
            use_container_width=True,
        )

    with action_col3:

        st.button(
            "Generate Report",
            use_container_width=True,
        )

    st.divider()

    # ---------------------------------------------------------
    # System Information
    # ---------------------------------------------------------

    with st.expander(
        "System Information",
        expanded=False,
    ):

        st.write("Application Version: 0.3.0")
        st.write("Platform: Sports Intelligence Platform")
        st.write("Environment: Development")
        st.write("Status: Operational")

        st.write(f"Organizations: {stats['organizations']}")
        st.write(f"Teams: {stats['teams']}")
        st.write(f"Players: {stats['players']}")
        st.write(f"Matches: {stats['matches']}")
        st.write(f"Events: {stats['events']}")

    AppLayout.end()