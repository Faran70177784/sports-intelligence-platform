"""
Event repository.
"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Event
from database.models import Match


class EventRepository:
    """Repository for event database operations."""

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

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
            .order_by(
                Event.match_id.desc(),
                Event.minute.asc(),
            )
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