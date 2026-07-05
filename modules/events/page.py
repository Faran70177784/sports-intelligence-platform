"""
Sports Intelligence Platform

Events management page.
"""

import streamlit as st

from services.event_service import EventService
from services.match_service import MatchService
from services.player_service import PlayerService
from shared.layouts import AppLayout


event_service = EventService()
match_service = MatchService()
player_service = PlayerService()


EVENT_TYPES = [
    "Goal",
    "Assist",
    "Yellow Card",
    "Red Card",
    "Substitution",
    "Shot",
    "Tackle",
    "Save",
]


def render() -> None:
    """Render Events page."""

    AppLayout.begin(
        title="Events",
        subtitle="Manage match events."
    )

    matches = match_service.get_all()
    players = player_service.get_all()

    if not matches:

        st.warning(
            "Create a match before adding events."
        )

        AppLayout.end()

        return

    if not players:

        st.warning(
            "Create players before adding events."
        )

        AppLayout.end()

        return

    # --------------------------------------------------

    st.subheader("➕ New Event")

    with st.form(
        "event_form",
        clear_on_submit=True,
    ):

        match = st.selectbox(
            "Match",
            matches,
            format_func=lambda m:
                f"{m.home.name} vs {m.away.name}",
        )

        player = st.selectbox(
            "Player",
            players,
            format_func=lambda p: p.full_name,
        )

        minute = st.number_input(
            "Minute",
            min_value=0,
            max_value=200,
            value=1,
        )

        event_type = st.selectbox(
            "Event Type",
            EVENT_TYPES,
        )

        submitted = st.form_submit_button(
            "Create Event",
            use_container_width=True,
        )

        if submitted:

            try:

                event_service.create(
                    match_id=match.id,
                    player_id=player.id,
                    minute=minute,
                    event_type=event_type,
                )

                st.success(
                    "Event created successfully."
                )

                st.rerun()

            except ValueError as error:

                st.error(str(error))

    st.divider()

    # --------------------------------------------------

    st.subheader("📋 Events")

    events = event_service.get_all()

    if not events:

        st.info(
            "No events found."
        )

    else:

        header = st.columns(
            [3, 2, 2, 2, 1]
        )

        header[0].markdown("**Match**")
        header[1].markdown("**Player**")
        header[2].markdown("**Minute**")
        header[3].markdown("**Type**")
        header[4].markdown("**Action**")

        st.divider()

        for event in events:

            c1, c2, c3, c4, c5 = st.columns(
                [3, 2, 2, 2, 1]
            )

            c1.write(
                f"{event.match.home.name} vs "
                f"{event.match.away.name}"
            )

            c2.write(event.player.full_name)

            c3.write(f"{event.minute}'")

            c4.write(event.event_type)

            if c5.button(
                "🗑️",
                key=f"delete_event_{event.id}",
            ):

                event_service.delete(
                    event.id
                )

                st.success(
                    "Event deleted successfully."
                )

                st.rerun()

    AppLayout.end()