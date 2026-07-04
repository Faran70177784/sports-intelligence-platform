"""
User repository.
"""

from typing import Optional

from sqlalchemy.orm import Session

from database.models import User
from database.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """
    Repository for User entities.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        super().__init__(db, User)

    def get_by_username(
        self,
        username: str,
    ) -> Optional[User]:

        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )

    def exists(
        self,
        username: str,
    ) -> bool:

        return self.get_by_username(username) is not None