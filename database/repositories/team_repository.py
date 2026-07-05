"""
Team repository.
"""

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Organization
from database.models import Player
from database.models import Team


class TeamRepository:
    """Repository for team database operations."""

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
        team: Team,
    ) -> Team:

        self.db.add(team)

        self.db.commit()

        self.db.refresh(team)

        return team

    def get_all(
        self,
    ) -> list[Team]:

        return (
            self.db.query(Team)
            .options(
                joinedload(Team.organization)
            )
            .order_by(Team.name)
            .all()
        )

    def get_by_name(
        self,
        name: str,
    ) -> Team | None:

        return (
            self.db.query(Team)
            .options(
                joinedload(Team.organization)
            )
            .filter(Team.name == name)
            .first()
        )

    def search(
        self,
        keyword: str,
    ) -> list[Team]:

        return (
            self.db.query(Team)
            .options(
                joinedload(Team.organization)
            )
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
            .options(
                joinedload(Team.organization)
            )
            .filter(
                Team.id == team_id
            )
            .first()
        )

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    def teams_by_country(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Team.country,
                func.count(Team.id),
            )
            .group_by(Team.country)
            .order_by(
                func.count(Team.id).desc()
            )
            .all()
        )

    def teams_by_organization(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Organization.name,
                func.count(Team.id),
            )
            .join(Organization)
            .group_by(
                Organization.name
            )
            .order_by(
                func.count(Team.id).desc()
            )
            .all()
        )

    def players_per_team(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Team.name,
                func.count(Player.id),
            )
            .outerjoin(Player)
            .group_by(
                Team.name
            )
            .order_by(
                func.count(Player.id).desc()
            )
            .all()
        )

    def total_teams(
        self,
    ) -> int:

        return (
            self.db.query(Team)
            .count()
        )