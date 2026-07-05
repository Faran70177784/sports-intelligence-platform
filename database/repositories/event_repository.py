"""
Event repository.
"""

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Event
from database.models import Match
from database.models import Player
from database.models import Team


class EventRepository:
    """Repository for event database operations."""

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
        event: Event,
    ) -> Event:

        self.db.add(event)

        self.db.commit()

        self.db.refresh(event)

        return event

    def get_all(
        self,
    ) -> list[Event]:

        return (
            self.db.query(Event)
            .options(
                joinedload(Event.player),
                joinedload(Event.match).joinedload(Match.home),
                joinedload(Event.match).joinedload(Match.away),
            )
            .order_by(Event.minute)
            .all()
        )

    def get_by_id(
        self,
        event_id: int,
    ) -> Event | None:

        return (
            self.db.query(Event)
            .options(
                joinedload(Event.player),
                joinedload(Event.match).joinedload(Match.home),
                joinedload(Event.match).joinedload(Match.away),
            )
            .filter(Event.id == event_id)
            .first()
        )

    def delete(
        self,
        event: Event,
    ) -> None:

        self.db.delete(event)

        self.db.commit()

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    def events_by_type(self) -> list[tuple]:

        return (
            self.db.query(
                Event.event_type,
                func.count(Event.id),
            )
            .group_by(Event.event_type)
            .order_by(func.count(Event.id).desc())
            .all()
        )

    def top_scorers(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Player.full_name,
                func.count(Event.id),
            )
            .join(Player)
            .filter(
                Event.event_type == "Goal"
            )
            .group_by(Player.full_name)
            .order_by(
                func.count(Event.id).desc()
            )
            .all()
        )

    def goals_by_team(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Team.name,
                func.count(Event.id),
            )
            .join(Player)
            .join(Team)
            .filter(
                Event.event_type == "Goal"
            )
            .group_by(Team.name)
            .order_by(
                func.count(Event.id).desc()
            )
            .all()
        )

    def assists_by_player(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Player.full_name,
                func.count(Event.id),
            )
            .join(Player)
            .filter(
                Event.event_type == "Assist"
            )
            .group_by(Player.full_name)
            .order_by(
                func.count(Event.id).desc()
            )
            .all()
        )