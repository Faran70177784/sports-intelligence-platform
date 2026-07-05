"""
Sports Intelligence Platform

Teams management page.
"""

import streamlit as st

from services.organization_service import OrganizationService
from services.team_service import TeamService
from shared.layouts import AppLayout


team_service = TeamService()
organization_service = OrganizationService()


def render() -> None:
    """Render Teams page."""

    AppLayout.begin(
        title="Teams",
        subtitle="Manage sports teams."
    )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    search = st.text_input(
        "🔍 Search Team",
        placeholder="Search by team name..."
    )

    st.divider()

    # --------------------------------------------------
    # Load Organizations
    # --------------------------------------------------

    organizations = organization_service.get_all()

    if not organizations:

        st.warning(
            "Please create an organization before creating teams."
        )

        AppLayout.end()

        return

    # --------------------------------------------------
    # Create Team
    # --------------------------------------------------

    st.subheader("➕ New Team")

    with st.form(
        "team_form",
        clear_on_submit=True,
    ):

        name = st.text_input(
            "Team Name"
        )

        country = st.text_input(
            "Country"
        )

        selected = st.selectbox(
            "Organization",
            organizations,
            format_func=lambda o: o.name,
        )

        submitted = st.form_submit_button(
            "Create Team",
            use_container_width=True,
        )

        if submitted:

            try:

                team_service.create(
                    name=name,
                    country=country,
                    organization_id=selected.id,
                )

                st.success(
                    "Team created successfully."
                )

                st.rerun()

            except ValueError as error:

                st.error(str(error))

    st.divider()

    # --------------------------------------------------
    # Teams List
    # --------------------------------------------------

    st.subheader("📋 Teams")

    if search.strip():

        teams = team_service.search(search)

    else:

        teams = team_service.get_all()

    if not teams:

        st.info(
            "No teams found."
        )

    else:

        header = st.columns([3, 2, 3, 1])

        header[0].markdown("**Team**")
        header[1].markdown("**Country**")
        header[2].markdown("**Organization**")
        header[3].markdown("**Action**")

        st.divider()

        for team in teams:

            col1, col2, col3, col4 = st.columns([3, 2, 3, 1])

            col1.write(team.name)
            col2.write(team.country)
            col3.write(team.organization.name)

            if col4.button(
                "🗑️",
                key=f"delete_team_{team.id}",
            ):

                team_service.delete(team.id)

                st.success(
                    "Team deleted successfully."
                )

                st.rerun()

    AppLayout.end()