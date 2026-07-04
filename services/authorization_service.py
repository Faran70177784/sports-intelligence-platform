"""
Authorization service.

Role-based access control.
"""

from auth.session_manager import SessionManager


class AuthorizationService:

    @staticmethod
    def has_role(role: str) -> bool:

        user = SessionManager.current_user()

        if user is None:
            return False

        return user.role == role

    @staticmethod
    def has_any_role(*roles: str) -> bool:

        user = SessionManager.current_user()

        if user is None:
            return False

        return user.role in roles

    @staticmethod
    def is_admin() -> bool:

        return AuthorizationService.has_role(
            "Administrator"
        )

    @staticmethod
    def is_analyst() -> bool:

        return AuthorizationService.has_role(
            "Analyst"
        )

    @staticmethod
    def is_coach() -> bool:

        return AuthorizationService.has_role(
            "Coach"
        )

    @staticmethod
    def is_scout() -> bool:

        return AuthorizationService.has_role(
            "Scout"
        )