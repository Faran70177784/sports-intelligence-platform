import streamlit as st

from components import LoginForm
from components import LogoutButton
from services.authentication_service import AuthenticationService

auth = AuthenticationService()

st.set_page_config(
    page_title="Authentication Test",
    layout="centered",
)

if not auth.is_authenticated():

    LoginForm().render()

else:

    user = auth.current_user()

    st.success(
        f"Welcome {user.username}"
    )

    st.write(
        f"Role: {user.role}"
    )

    LogoutButton().render()