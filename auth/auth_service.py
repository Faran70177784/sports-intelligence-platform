"""
Authentication service.
"""

from typing import Optional

from auth.security import SecurityManager
from database.db import get_db
from database.models import User
from database.repositories.user_repository import UserRepository


class AuthenticationService:

    def __init__(self) -> None:
        self.security = SecurityManager()

    def authenticate(
        self,
        username: str,
        password: str,
    ) -> Optional[User]:

        with get_db() as db:

            repository = UserRepository(db)

            user = repository.get_by_username(
                username
            )

            if user is None:
                return None

            if not self.security.verify_password(
                password,
                user.password,
            ):
                return None

            return user

    def create_user(
        self,
        username: str,
        password: str,
        role: str = "Analyst",
    ) -> User:

        with get_db() as db:

            repository = UserRepository(db)

            hashed_password = self.security.hash_password(
                password
            )

            user = User(
                username=username,
                password=hashed_password,
                role=role,
            )

            return repository.create(user)