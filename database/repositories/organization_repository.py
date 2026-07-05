"""
Organization repository.
"""

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from database.models import Organization
from database.models import Team


class OrganizationRepository:
    """Repository for organization database operations."""

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
        organization: Organization,
    ) -> Organization:

        self.db.add(organization)

        self.db.commit()

        self.db.refresh(organization)

        return organization

    def get_all(
        self,
    ) -> list[Organization]:

        return (
            self.db.query(Organization)
            .options(
                joinedload(Organization.teams)
            )
            .order_by(Organization.name)
            .all()
        )

    def get_by_id(
        self,
        organization_id: int,
    ) -> Organization | None:

        return (
            self.db.query(Organization)
            .options(
                joinedload(Organization.teams)
            )
            .filter(
                Organization.id == organization_id
            )
            .first()
        )

    def get_by_name(
        self,
        name: str,
    ) -> Organization | None:

        return (
            self.db.query(Organization)
            .filter(
                Organization.name == name
            )
            .first()
        )

    def search(
        self,
        keyword: str,
    ) -> list[Organization]:

        return (
            self.db.query(Organization)
            .filter(
                Organization.name.ilike(
                    f"%{keyword}%"
                )
            )
            .order_by(Organization.name)
            .all()
        )

    def delete(
        self,
        organization: Organization,
    ) -> None:

        self.db.delete(organization)

        self.db.commit()

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    def organizations_by_country(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Organization.country,
                func.count(Organization.id),
            )
            .group_by(
                Organization.country
            )
            .order_by(
                func.count(Organization.id).desc()
            )
            .all()
        )

    def teams_per_organization(
        self,
    ) -> list[tuple]:

        return (
            self.db.query(
                Organization.name,
                func.count(Team.id),
            )
            .outerjoin(Team)
            .group_by(
                Organization.name
            )
            .order_by(
                func.count(Team.id).desc()
            )
            .all()
        )

    def total_organizations(
        self,
    ) -> int:

        return (
            self.db.query(
                Organization
            ).count()
        )