"""
Sports Intelligence Platform

Players management page.
"""

import streamlit as st

from services.player_service import PlayerService
from services.team_service import TeamService
from shared.layouts import AppLayout


player_service = PlayerService()
team_service = TeamService()


def render() -> None:
    """Render Players page."""

    AppLayout.begin(
        title="Players",
        subtitle="Manage sports players."
    )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    search = st.text_input(
        "🔍 Search Player",
        placeholder="Search by player name..."
    )

    st.divider()

    # --------------------------------------------------
    # Load Teams
    # --------------------------------------------------

    teams = team_service.get_all()

    if not teams:

        st.warning(
            "Please create a team before creating players."
        )

        AppLayout.end()

        return

    # --------------------------------------------------
    # Create Player
    # --------------------------------------------------

    st.subheader("➕ New Player")

    with st.form(
        "player_form",
        clear_on_submit=True,
    ):

        full_name = st.text_input(
            "Player Name"
        )

        position = st.text_input(
            "Position"
        )

        selected_team = st.selectbox(
            "Team",
            teams,
            format_func=lambda team: team.name,
        )

        submitted = st.form_submit_button(
            "Create Player",
            use_container_width=True,
        )

        if submitted:

            try:

                player_service.create(
                    full_name=full_name,
                    position=position,
                    team_id=selected_team.id,
                )

                st.success(
                    "Player created successfully."
                )

                st.rerun()

            except ValueError as error:

                st.error(str(error))

    st.divider()

    # --------------------------------------------------
    # Players List
    # --------------------------------------------------

    st.subheader("📋 Players")

    if search.strip():

        players = player_service.search(search)

    else:

        players = player_service.get_all()

    if not players:

        st.info(
            "No players found."
        )

    else:

        header = st.columns([3, 2, 3, 1])

        header[0].markdown("**Player**")
        header[1].markdown("**Position**")
        header[2].markdown("**Team**")
        header[3].markdown("**Action**")

        st.divider()

        for player in players:

            col1, col2, col3, col4 = st.columns([3, 2, 3, 1])

            col1.write(player.full_name)
            col2.write(player.position)
            col3.write(player.team.name)

            if col4.button(
                "🗑️",
                key=f"delete_player_{player.id}",
            ):

                player_service.delete(
                    player.id
                )

                st.success(
                    "Player deleted successfully."
                )

                st.rerun()

    AppLayout.end()