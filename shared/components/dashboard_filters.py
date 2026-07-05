"""
Reusable dashboard filters.
"""

from typing import Any

import streamlit as st


class DashboardFilters:
    """Reusable dashboard filter component."""

    @staticmethod
    def render(
        organizations: list[Any],
        teams: list[Any],
        matches: list[Any],
    ) -> dict[str, Any]:
        """
        Render dashboard filters.

        Returns
        -------
        dict
            Selected filter values.
        """

        st.subheader("Dashboard Filters")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            organization = st.selectbox(
                "Organization",
                ["All"] + organizations,
            )

        with col2:

            team = st.selectbox(
                "Team",
                ["All"] + teams,
            )

        with col3:

            match = st.selectbox(
                "Match",
                ["All"] + matches,
            )

        with col4:

            event_type = st.selectbox(
                "Event Type",
                [
                    "All",
                    "Goal",
                    "Assist",
                    "Yellow Card",
                    "Red Card",
                    "Substitution",
                ],
            )

        return {
            "organization": organization,
            "team": team,
            "match": match,
            "event_type": event_type,
        }