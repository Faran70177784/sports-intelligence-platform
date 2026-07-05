"""
Player repository.
"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Player


class PlayerRepository:
    """Repository for player database operations."""

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

    def create(
        self,
        player: Player,
    ) -> Player:

        self.db.add(player)

        self.db.commit()

        self.db.refresh(player)

        return player

    def get_all(
        self,
    ) -> list[Player]:

        return (
            self.db.query(Player)
            .options(joinedload(Player.team))
            .order_by(Player.full_name)
            .all()
        )

    def get_by_id(
        self,
        player_id: int,
    ) -> Player | None:

        return (
            self.db.query(Player)
            .options(joinedload(Player.team))
            .filter(Player.id == player_id)
            .first()
        )

    def get_by_name(
        self,
        full_name: str,
    ) -> Player | None:

        return (
            self.db.query(Player)
            .options(joinedload(Player.team))
            .filter(Player.full_name == full_name)
            .first()
        )

    def search(
        self,
        keyword: str,
    ) -> list[Player]:

        return (
            self.db.query(Player)
            .options(joinedload(Player.team))
            .filter(
                Player.full_name.ilike(
                    f"%{keyword}%"
                )
            )
            .order_by(Player.full_name)
            .all()
        )

    def delete(
        self,
        player: Player,
    ) -> None:

        self.db.delete(player)

        self.db.commit()