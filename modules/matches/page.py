"""
Sports Intelligence Platform

Matches management page.
"""

from datetime import date

import streamlit as st

from services.match_service import MatchService
from services.team_service import TeamService
from shared.layouts import AppLayout


match_service = MatchService()
team_service = TeamService()


def render() -> None:
    """Render Matches page."""

    AppLayout.begin(
        title="Matches",
        subtitle="Manage sports matches.",
    )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    search = st.text_input(
        "🔍 Search Match",
        placeholder="Search by team name...",
    )

    st.divider()

    # --------------------------------------------------
    # Load Teams
    # --------------------------------------------------

    teams = team_service.get_all()

    if len(teams) < 2:

        st.warning(
            "Please create at least two teams before creating matches."
        )

        AppLayout.end()

        return

    # --------------------------------------------------
    # Create Match
    # --------------------------------------------------

    st.subheader("➕ New Match")

    with st.form(
        "match_form",
        clear_on_submit=True,
    ):

        home_team = st.selectbox(
            "Home Team",
            teams,
            format_func=lambda t: t.name,
        )

        away_team = st.selectbox(
            "Away Team",
            teams,
            index=1,
            format_func=lambda t: t.name,
        )

        match_date = st.date_input(
            "Match Date",
            value=date.today(),
        )

        submitted = st.form_submit_button(
            "Create Match",
            use_container_width=True,
        )

        if submitted:

            try:

                match_service.create(
                    home_team=home_team.id,
                    away_team=away_team.id,
                    match_date=match_date,
                )

                st.success(
                    "Match created successfully."
                )

                st.rerun()

            except ValueError as error:

                st.error(str(error))

    st.divider()

    # --------------------------------------------------
    # Matches List
    # --------------------------------------------------

    st.subheader("📋 Matches")

    matches = match_service.get_all()

    if search.strip():

        keyword = search.lower()

        matches = [
            match
            for match in matches
            if keyword in match.home.name.lower()
            or keyword in match.away.name.lower()
        ]

    if not matches:

        st.info(
            "No matches found."
        )

    else:

        header = st.columns([3, 3, 2, 1])

        header[0].markdown("**Home Team**")
        header[1].markdown("**Away Team**")
        header[2].markdown("**Date**")
        header[3].markdown("**Action**")

        st.divider()

        for match in matches:

            col1, col2, col3, col4 = st.columns([3, 3, 2, 1])

            col1.write(match.home.name)
            col2.write(match.away.name)
            col3.write(
                match.match_date.strftime("%d %b %Y")
            )

            if col4.button(
                "🗑️",
                key=f"delete_match_{match.id}",
            ):

                match_service.delete(match.id)

                st.success(
                    "Match deleted successfully."
                )

                st.rerun()

    AppLayout.end()