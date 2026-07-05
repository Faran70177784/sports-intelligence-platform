"""
Team repository.
"""

from sqlalchemy.orm import Session, joinedload

from database.models import Team


class TeamRepository:
    """Repository for team database operations."""

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

    def create(
        self,
        team: Team,
    ) -> Team:

        self.db.add(team)

        self.db.commit()

        self.db.refresh(team)

        return team

    def get_all(self) -> list[Team]:

        return (
            self.db.query(Team)
            .options(joinedload(Team.organization))
            .order_by(Team.name)
            .all()
        )

    def get_by_name(
        self,
        name: str,
    ) -> Team | None:

        return (
            self.db.query(Team)
            .options(joinedload(Team.organization))
            .filter(Team.name == name)
            .first()
        )

    def search(
        self,
        keyword: str,
    ) -> list[Team]:

        return (
            self.db.query(Team)
            .options(joinedload(Team.organization))
            .filter(
                Team.name.ilike(
                    f"%{keyword}%"
                )
            )
            .order_by(Team.name)
            .all()
        )

    def delete(
        self,
        team: Team,
    ) -> None:

        self.db.delete(team)

        self.db.commit()

    def get_by_id(
        self,
        team_id: int,
    ) -> Team | None:

        return (
            self.db.query(Team)
            .options(joinedload(Team.organization))
            .filter(
                Team.id == team_id
            )
            .first()
        )