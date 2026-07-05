"""
Team business service.
"""

from database.db import get_db
from database.models import Team
from database.repositories.team_repository import TeamRepository


class TeamService:
    """Handles team business logic."""

    def create(
        self,
        name: str,
        country: str,
        organization_id: int,
    ) -> Team:

        with get_db() as db:

            repository = TeamRepository(db)

            name = name.strip()
            country = country.strip()

            if repository.get_by_name(name):

                raise ValueError(
                    "Team already exists."
                )

            team = Team(
                name=name,
                country=country,
                organization_id=organization_id,
            )

            return repository.create(team)

    def get_all(self) -> list[Team]:

        with get_db() as db:

            repository = TeamRepository(db)

            return repository.get_all()

    def search(
        self,
        keyword: str,
    ) -> list[Team]:

        with get_db() as db:

            repository = TeamRepository(db)

            return repository.search(keyword)

    def delete(
        self,
        team_id: int,
    ) -> None:

        with get_db() as db:

            repository = TeamRepository(db)

            team = repository.get_by_id(team_id)

            if team:

                repository.delete(team)