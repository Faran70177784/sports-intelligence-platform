"""
Player business service.
"""

from database.db import get_db
from database.models import Player
from database.repositories.player_repository import PlayerRepository


class PlayerService:
    """Business logic for players."""

    def get_all(self) -> list[Player]:

        with get_db() as db:

            return PlayerRepository(db).get_all()

    def get_by_id(
        self,
        player_id: int,
    ) -> Player | None:

        with get_db() as db:

            return PlayerRepository(db).get_by_id(
                player_id
            )

    def search(
        self,
        keyword: str,
    ) -> list[Player]:

        with get_db() as db:

            return PlayerRepository(db).search(
                keyword
            )

    def create(
        self,
        full_name: str,
        position: str,
        team_id: int,
    ) -> Player:

        with get_db() as db:

            repository = PlayerRepository(db)

            player = Player(
                full_name=full_name,
                position=position,
                team_id=team_id,
            )

            return repository.create(player)

    def delete(
        self,
        player_id: int,
    ) -> None:

        with get_db() as db:

            repository = PlayerRepository(db)

            player = repository.get_by_id(
                player_id
            )

            if player is not None:

                repository.delete(player)