"""
Event business service.
"""

from database.db import get_db
from database.models import Event
from database.repositories.event_repository import EventRepository


class EventService:
    """Business logic for events."""

    def get_all(self) -> list[Event]:

        with get_db() as db:

            return EventRepository(db).get_all()

    def get_by_id(
        self,
        event_id: int,
    ) -> Event | None:

        with get_db() as db:

            return EventRepository(db).get_by_id(
                event_id
            )

    def create(
        self,
        match_id: int,
        player_id: int,
        minute: int,
        event_type: str,
    ) -> Event:

        if minute < 0:

            raise ValueError(
                "Minute cannot be negative."
            )

        with get_db() as db:

            repository = EventRepository(db)

            event = Event(
                match_id=match_id,
                player_id=player_id,
                minute=minute,
                event_type=event_type,
            )

            return repository.create(event)

    def delete(
        self,
        event_id: int,
    ) -> None:

        with get_db() as db:

            repository = EventRepository(db)

            event = repository.get_by_id(
                event_id
            )

            if event is not None:

                repository.delete(event)