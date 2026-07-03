"""
Home page for the Sports Analytics Dashboard Platform.
"""

import streamlit as st
from config import settings


def render():
    """
    Render the Home page.
    """

    st.title("🏆 Sports Analytics Dashboard Platform")

    st.caption(
        f"Version {settings.app_version}"
    )

    st.divider()

    st.markdown(
        """
Welcome to the **Sports Analytics Dashboard Platform**.

This platform is being developed as a commercial-grade analytics solution
for multiple sports including:

- 🏒 Hockey
- ⚽ Football
- 🏀 Basketball
- 🏏 Cricket
- ⚾ Baseball

---

### Current Development Stage

Foundation & Core Architecture

---

### Upcoming Features

- Interactive Dashboard
- Team Analytics
- Player Analytics
- Match Analytics
- Reports
- Data Upload
- AI Insights
- Authentication
"""
    )