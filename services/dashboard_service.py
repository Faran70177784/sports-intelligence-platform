"""
Dashboard analytics service.
"""

from database.db import get_db
from database.models import Event
from database.models import Match
from database.models import Organization
from database.models import Player
from database.models import Team


class DashboardService:
    """Provides dashboard statistics."""

    def get_statistics(self) -> dict[str, int]:

        with get_db() as db:

            return {
                "organizations": db.query(Organization).count(),
                "teams": db.query(Team).count(),
                "players": db.query(Player).count(),
                "matches": db.query(Match).count(),
                "events": db.query(Event).count(),
            }