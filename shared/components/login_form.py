"""
Professional login component.
"""

import streamlit as st

from services.authentication_service import AuthenticationService


class LoginForm:

    def __init__(self):

        self.auth = AuthenticationService()

    def render(self) -> bool:
        """
        Render login form.

        Returns:
            True if authenticated.
        """

        st.title("🏆 Sports Intelligence Platform")

        st.markdown(
            "### Secure Login"
        )

        with st.form(
            "login_form",
            clear_on_submit=False,
        ):

            username = st.text_input(
                "Username"
            )

            password = st.text_input(
                "Password",
                type="password",
            )

            submitted = st.form_submit_button(
                "Sign In",
                use_container_width=True,
            )

        if submitted:

            success = self.auth.login(
                username,
                password,
            )

            if success:

                st.success(
                    "Login successful."
                )

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

        return self.auth.is_authenticated()