"""
Match business service.
"""

from datetime import date

from database.db import get_db
from database.models import Match
from database.repositories import MatchRepository


class MatchService:
    """Business logic for matches."""

    def get_all(
        self,
    ) -> list[Match]:

        with get_db() as db:

            return (
                MatchRepository(db)
                .get_all()
            )

    def get_by_id(
        self,
        match_id: int,
    ) -> Match | None:

        with get_db() as db:

            return (
                MatchRepository(db)
                .get_by_id(match_id)
            )

    def create(
        self,
        home_team: int,
        away_team: int,
        match_date: date,
    ) -> Match:
        """
        Create a new match.
        """

        if home_team == away_team:
            raise ValueError(
                "Home and Away teams must be different."
            )

        with get_db() as db:

            repository = MatchRepository(db)

            match = Match(
                home_team=home_team,
                away_team=away_team,
                match_date=match_date,
            )

            return repository.create(match)

    def delete(
        self,
        match_id: int,
    ) -> None:

        with get_db() as db:

            repository = MatchRepository(db)

            match = repository.get_by_id(
                match_id
            )

            if match is None:
                raise ValueError(
                    "Match not found."
                )

            repository.delete(match)