"""
Organization repository.
"""

from sqlalchemy.orm import Session

from database.models import Organization


class OrganizationRepository:
    """Repository for organization database operations."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(
        self,
        organization: Organization,
    ) -> Organization:

        self.db.add(organization)
        self.db.commit()
        self.db.refresh(organization)

        return organization

    def get_all(self) -> list[Organization]:

        return (
            self.db.query(Organization)
            .order_by(Organization.name)
            .all()
        )

    def get_by_id(
        self,
        organization_id: int,
    ) -> Organization | None:

        return (
            self.db.query(Organization)
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
                Organization.name.ilike(f"%{keyword}%")
            )
            .order_by(Organization.name)
            .all()
        )

    def update(self) -> None:

        self.db.commit()

    def delete(
        self,
        organization: Organization,
    ) -> None:

        self.db.delete(organization)
        self.db.commit()