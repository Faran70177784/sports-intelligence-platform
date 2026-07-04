"""
Session management for Streamlit.
"""

import streamlit as st


class SessionManager:

    USER_KEY = "current_user"

    @staticmethod
    def login(user) -> None:
        st.session_state[SessionManager.USER_KEY] = user

    @staticmethod
    def logout() -> None:
        st.session_state.pop(
            SessionManager.USER_KEY,
            None,
        )

    @staticmethod
    def is_authenticated() -> bool:
        return SessionManager.USER_KEY in st.session_state

    @staticmethod
    def current_user():
        return st.session_state.get(
            SessionManager.USER_KEY
        )