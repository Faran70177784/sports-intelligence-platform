"""
Team repository.
"""

from database.models.team import Team
from database.repositories.base_repository import BaseRepository


class TeamRepository(BaseRepository[Team]):

    def __init__(self, db):

        super().__init__(db, Team)

    def get_by_name(self, name: str):

        return (
            self.db.query(Team)
            .filter(Team.name == name)
            .first()
        )