"""
Match repository.
"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Match


class MatchRepository:
    """Repository for match database operations."""

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

    def get_all(self) -> list[Match]:

        return (
            self.db.query(Match)
            .options(
                joinedload(Match.home),
                joinedload(Match.away),
            )
            .order_by(Match.match_date.desc())
            .all()
        )

    def get_by_id(
        self,
        match_id: int,
    ) -> Match | None:

        return (
            self.db.query(Match)
            .options(
                joinedload(Match.home),
                joinedload(Match.away),
            )
            .filter(Match.id == match_id)
            .first()
        )

    def create(
        self,
        match: Match,
    ) -> Match:

        self.db.add(match)

        self.db.commit()

        self.db.refresh(match)

        return match

    def delete(
        self,
        match: Match,
    ) -> None:

        self.db.delete(match)

        self.db.commit()