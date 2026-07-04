"""
Authentication business service.
"""

from typing import Optional

from auth.auth_service import AuthenticationService as AuthBackend
from auth.session_manager import SessionManager
from database.models import User


class AuthenticationService:
    """
    High-level authentication service.

    Handles login/logout/session operations.
    """

    def __init__(self) -> None:
        self.backend = AuthBackend()

    def login(
        self,
        username: str,
        password: str,
    ) -> bool:

        user: Optional[User] = self.backend.authenticate(
            username=username,
            password=password,
        )

        if user is None:
            return False

        SessionManager.login(user)

        return True

    def logout(self) -> None:
        SessionManager.logout()

    def current_user(self) -> Optional[User]:
        return SessionManager.current_user()

    def is_authenticated(self) -> bool:
        return SessionManager.is_authenticated()