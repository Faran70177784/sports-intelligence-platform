"""
Sports Intelligence Platform

File: page.py
Author: Syed Faran Ali

Description:
Dashboard module for the Sports Intelligence Platform.
Displays executive KPIs, analytics, filters,
recent activity and quick actions.
"""

import streamlit as st

from services.analytics_service import AnalyticsService
from services.match_service import MatchService
from services.organization_service import OrganizationService
from services.team_service import TeamService

from shared.components import (
    ActivityCard,
    AnalyticsCharts,
    DashboardFilters,
    KPICard,
    SectionTitle,
)
from shared.layouts import AppLayout


analytics_service = AnalyticsService()

organization_service = OrganizationService()

team_service = TeamService()

match_service = MatchService()


def render() -> None:
    """
    Render Dashboard page.
    """

    AppLayout.begin(
        title="Dashboard",
        subtitle="Executive overview of the Sports Intelligence Platform."
    )

    # ---------------------------------------------------------
    # Load Dashboard Data
    # ---------------------------------------------------------

    analytics = analytics_service.dashboard_statistics()

    organizations = organization_service.get_all()

    teams = team_service.get_all()

    matches = match_service.get_all()

    organization_options = [
        organization.name
        for organization in organizations
    ]

    team_options = [
        team.name
        for team in teams
    ]

    match_options = [
        f"{match.home.name} vs {match.away.name}"
        for match in matches
    ]

    # ---------------------------------------------------------
    # KPI Cards
    # ---------------------------------------------------------

    SectionTitle.render("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        KPICard.render(
            title="Organizations",
            value=str(
                analytics["organizations"]
            ),
        )

    with col2:

        KPICard.render(
            title="Teams",
            value=str(
                analytics["teams"]
            ),
        )

    with col3:

        KPICard.render(
            title="Players",
            value=str(
                analytics["players"]
            ),
        )

    with col4:

        KPICard.render(
            title="Matches",
            value=str(
                analytics["matches"]
            ),
        )

    st.divider()

    # ---------------------------------------------------------
    # Dashboard Filters
    # ---------------------------------------------------------

    filters = DashboardFilters.render(
        organizations=organization_options,
        teams=team_options,
        matches=match_options,
    )

    st.divider()

    # ---------------------------------------------------------
    # Analytics Charts
    # ---------------------------------------------------------

    SectionTitle.render(
        "Analytics Overview"
    )

    col1, col2 = st.columns(2)

    with col1:

        AnalyticsCharts.pie_chart(
            data=[
                ("Organizations", analytics["organizations"]),
                ("Teams", analytics["teams"]),
                ("Players", analytics["players"]),
                ("Matches", analytics["matches"]),
            ],
            title="Platform Data Distribution",
        )

    with col2:

        AnalyticsCharts.bar_chart(
            data=[
                ("Organizations", analytics["organizations"]),
                ("Teams", analytics["teams"]),
                ("Players", analytics["players"]),
                ("Matches", analytics["matches"]),
            ],
            title="Platform Statistics",
            x_title="Category",
            y_title="Count",
        )

    st.divider()

    # ---------------------------------------------------------
    # Recent Activity
    # ---------------------------------------------------------

    SectionTitle.render(
        "Recent Activity"
    )

    ActivityCard.render(
        (
            "Dashboard filters are active. "
            "Interactive analytics will be available "
            "in the next update."
        )
    )

    st.divider()

    # ---------------------------------------------------------
    # Quick Actions
    # ---------------------------------------------------------

    SectionTitle.render(
        "Quick Actions"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.button(
            "Import Data",
            use_container_width=True,
        )

    with col2:

        st.button(
            "Open Analytics",
            use_container_width=True,
        )

    with col3:

        st.button(
            "Generate Report",
            use_container_width=True,
        )

    st.divider()

    # ---------------------------------------------------------
    # System Information
    # ---------------------------------------------------------

    with st.expander(
        "System Information"
    ):

        st.write(
            "Application Version: 0.4.0"
        )

        st.write(
            "Platform: Sports Intelligence Platform"
        )

        st.write(
            "Environment: Development"
        )

        st.write(
            "Status: Operational"
        )

        st.write(
            f"Organizations: {analytics['organizations']}"
        )

        st.write(
            f"Teams: {analytics['teams']}"
        )

        st.write(
            f"Players: {analytics['players']}"
        )

        st.write(
            f"Matches: {analytics['matches']}"
        )

    AppLayout.end()