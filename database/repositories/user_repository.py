"""
User repository.

Handles database operations for User entities.
"""

from typing import Optional

from sqlalchemy.orm import Session

from database.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_username(
        self,
        username: str,
    ) -> Optional[User]:

        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )

    def create(
        self,
        user: User,
    ) -> User:

        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)

        return user

    def exists(
        self,
        username: str,
    ) -> bool:

        return (
            self.get_by_username(username)
            is not None
        )