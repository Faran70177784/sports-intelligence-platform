"""
Team repository.
"""

from typing import Optional

from sqlalchemy.orm import Session

from database.models import Team
from database.repositories.base_repository import BaseRepository


class TeamRepository(BaseRepository[Team]):
    """
    Repository for Team entities.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        super().__init__(db, Team)

    def get_by_name(
        self,
        name: str,
    ) -> Optional[Team]:

        return (
            self.db.query(Team)
            .filter(Team.name == name)
            .first()
        )