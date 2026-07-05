"""
Analytics business service.
"""

from sqlalchemy import func

from database.db import get_db
from database.models import (
    Event,
    Match,
    Organization,
    Player,
    Team,
)


class AnalyticsService:
    """Business logic for analytics."""

    def dashboard_statistics(self) -> dict[str, int]:
        """
        Return dashboard KPI statistics.
        """

        with get_db() as db:

            return {
                "organizations": db.query(Organization).count(),
                "teams": db.query(Team).count(),
                "players": db.query(Player).count(),
                "matches": db.query(Match).count(),
                "events": db.query(Event).count(),
            }

    def event_distribution(self) -> list[tuple[str, int]]:
        """
        Return event distribution.
        """

        with get_db() as db:

            return (
                db.query(
                    Event.event_type,
                    func.count(Event.id),
                )
                .group_by(Event.event_type)
                .all()
            )

    def players_per_team(self) -> list[tuple[str, int]]:
        """
        Return number of players in each team.
        """

        with get_db() as db:

            return (
                db.query(
                    Team.name,
                    func.count(Player.id),
                )
                .join(Player)
                .group_by(Team.id)
                .order_by(Team.name)
                .all()
            )

    def top_scorers(self) -> list[tuple[str, int]]:
        """
        Return players ranked by goals.
        """

        with get_db() as db:

            return (
                db.query(
                    Player.full_name,
                    func.count(Event.id),
                )
                .join(Event)
                .filter(Event.event_type == "Goal")
                .group_by(Player.id)
                .order_by(func.count(Event.id).desc())
                .all()
            )