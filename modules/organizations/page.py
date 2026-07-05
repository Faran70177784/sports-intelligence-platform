"""
Sports Intelligence Platform

Organizations management page.
"""

import streamlit as st

from services.organization_service import OrganizationService
from shared.layouts import AppLayout


service = OrganizationService()


def render() -> None:
    """Render Organizations page."""

    AppLayout.begin(
        title="Organizations",
        subtitle="Manage sports organizations."
    )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    search = st.text_input(
        "🔍 Search Organization",
        placeholder="Search by organization name..."
    )

    st.divider()

    # --------------------------------------------------
    # Create Organization
    # --------------------------------------------------

    st.subheader("➕ New Organization")

    with st.form(
        "organization_form",
        clear_on_submit=True,
    ):

        name = st.text_input(
            "Organization Name"
        )

        country = st.text_input(
            "Country"
        )

        organization_type = st.selectbox(
            "Organization Type",
            [
                "Club",
                "Federation",
                "League",
                "University",
                "Academy",
                "Association",
            ],
        )

        submitted = st.form_submit_button(
            "Create Organization",
            use_container_width=True,
        )

        if submitted:

            try:

                service.create(
                    name=name,
                    country=country,
                    organization_type=organization_type,
                )

                st.success(
                    "Organization created successfully."
                )

                st.rerun()

            except ValueError as error:

                st.error(str(error))

    st.divider()

    # --------------------------------------------------
    # Organizations List
    # --------------------------------------------------

    st.subheader("📋 Organizations")

    if search.strip():

        organizations = service.search(search)

    else:

        organizations = service.get_all()

    if not organizations:

        st.info(
            "No organizations found."
        )

    else:

        for organization in organizations:

            col1, col2, col3, col4 = st.columns(
                [4, 2, 2, 1]
            )

            with col1:
                st.write(f"**{organization.name}**")

            with col2:
                st.write(organization.country)

            with col3:
                st.write(
                    organization.organization_type
                )

            with col4:

                if st.button(
                    "🗑️",
                    key=f"delete_{organization.id}",
                ):

                    service.delete(
                        organization.id
                    )

                    st.success(
                        "Organization deleted."
                    )

                    st.rerun()

    AppLayout.end()