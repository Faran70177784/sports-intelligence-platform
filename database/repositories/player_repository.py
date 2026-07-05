"""
Player repository.
"""

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Player
from database.models import Team


class PlayerRepository:
    """Repository for player database operations."""

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
            .options(
                joinedload(Player.team)
            )
            .order_by(Player.full_name)
            .all()
        )

    def get_by_id(
        self,
        player_id: int,
    ) -> Player | None:

        return (
            self.db.query(Player)
            .options(
                joinedload(Player.team)
            )
            .filter(Player.id == player_id)
            .first()
        )

    def get_by_name(
        self,
        full_name: str,
    ) -> Player | None:

        return (
            self.db.query(Player)
            .options(
                joinedload(Player.team)
            )
            .filter(
                Player.full_name == full_name
            )
            .first()
        )

    def search(
        self,
        keyword: str,
    ) -> list[Player]:

        return (
            self.db.query(Player)
            .options(
                joinedload(Player.team)
            )
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

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    def players_by_position(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Player.position,
                func.count(Player.id),
            )
            .group_by(Player.position)
            .order_by(
                func.count(Player.id).desc()
            )
            .all()
        )

    def players_by_team(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Team.name,
                func.count(Player.id),
            )
            .join(Team)
            .group_by(Team.name)
            .order_by(
                func.count(Player.id).desc()
            )
            .all()
        )

    def total_players(
        self,
    ) -> int:

        return (
            self.db.query(Player)
            .count()
        )