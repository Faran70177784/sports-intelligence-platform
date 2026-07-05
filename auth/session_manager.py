"""
Session management for Streamlit.
"""

import streamlit as st


class SessionManager:
    """Manage authenticated user session."""

    USER_KEY = "current_user"

    @staticmethod
    def login(user) -> None:
        """
        Store only serializable user information.
        Never store SQLAlchemy ORM objects.
        """

        st.session_state[SessionManager.USER_KEY] = {
            "id": user.id,
            "username": user.username,
            "role": user.role,
        }

    @staticmethod
    def logout() -> None:
        """
        Clear the authenticated session.
        """

        st.session_state.pop(
            SessionManager.USER_KEY,
            None,
        )

    @staticmethod
    def is_authenticated() -> bool:
        """
        Check whether a user is logged in.
        """

        return SessionManager.USER_KEY in st.session_state

    @staticmethod
    def current_user():
        """
        Return the current logged-in user dictionary.
        """

        return st.session_state.get(
            SessionManager.USER_KEY
        )