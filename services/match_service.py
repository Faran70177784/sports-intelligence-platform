"""
Match business service.
"""

from database.db import get_db
from database.models import Match
from database.repositories.match_repository import MatchRepository


class MatchService:
    """Business logic for matches."""

    def get_all(self) -> list[Match]:

        with get_db() as db:

            return MatchRepository(db).get_all()

    def get_by_id(
        self,
        match_id: int,
    ) -> Match | None:

        with get_db() as db:

            return MatchRepository(db).get_by_id(match_id)

    def create(
        self,
        match: Match,
    ) -> Match:

        with get_db() as db:

            return MatchRepository(db).create(match)

    def delete(
        self,
        match: Match,
    ) -> None:

        with get_db() as db:

            MatchRepository(db).delete(match)