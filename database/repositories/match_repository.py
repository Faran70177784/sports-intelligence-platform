"""
Match repository.
"""

from sqlalchemy import extract
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Match
from database.models import Team


class MatchRepository:
    """Repository for match database operations."""

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def create(
        self,
        match: Match,
    ) -> Match:

        self.db.add(match)

        self.db.commit()

        self.db.refresh(match)

        return match

    def get_all(
        self,
    ) -> list[Match]:

        return (
            self.db.query(Match)
            .options(
                joinedload(Match.home),
                joinedload(Match.away),
            )
            .order_by(
                Match.match_date.desc()
            )
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
            .filter(
                Match.id == match_id
            )
            .first()
        )

    def delete(
        self,
        match: Match,
    ) -> None:

        self.db.delete(match)

        self.db.commit()

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    def total_matches(
        self,
    ) -> int:

        return (
            self.db.query(Match)
            .count()
        )

    def matches_by_year(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                extract(
                    "year",
                    Match.match_date,
                ),
                func.count(Match.id),
            )
            .group_by(
                extract(
                    "year",
                    Match.match_date,
                )
            )
            .order_by(
                extract(
                    "year",
                    Match.match_date,
                )
            )
            .all()
        )

    def matches_by_home_team(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Team.name,
                func.count(Match.id),
            )
            .join(
                Match,
                Match.home_team == Team.id,
            )
            .group_by(
                Team.name
            )
            .order_by(
                func.count(Match.id).desc()
            )
            .all()
        )