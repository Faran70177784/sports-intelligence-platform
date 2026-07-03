"""
Sidebar component.
"""

import streamlit as st


def render():
    """
    Render application sidebar.
    """

    with st.sidebar:

        st.title("🏆 SADP")

        st.caption("Sports Analytics Platform")

        st.divider()

        st.success("Sprint 2")

        st.write("Version 0.1.0")

        st.divider()

        st.info(
            "Commercial Development Edition"
        )