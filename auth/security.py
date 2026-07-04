"""
Security utilities.

Provides password hashing and verification.
"""

from passlib.context import CryptContext


class SecurityManager:
    """
    Password security manager.
    """

    def __init__(self) -> None:
        self.password_context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto",
        )

    def hash_password(self, password: str) -> str:
        """
        Hash a plain-text password.
        """
        return self.password_context.hash(password)

    def verify_password(
        self,
        plain_password: str,
        hashed_password: str,
    ) -> bool:
        """
        Verify a password.
        """
        return self.password_context.verify(
            plain_password,
            hashed_password,
        )