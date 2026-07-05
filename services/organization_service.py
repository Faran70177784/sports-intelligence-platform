"""
Organization business service.
"""

from database.db import get_db
from database.models import Organization
from database.repositories.organization_repository import (
    OrganizationRepository,
)


class OrganizationService:
    """Handles organization business logic."""

    def create(
        self,
        name: str,
        country: str,
        organization_type: str,
    ) -> Organization:

        with get_db() as db:

            repository = OrganizationRepository(db)

            name = name.strip()
            country = country.strip()

            if repository.get_by_name(name):

                raise ValueError(
                    "Organization already exists."
                )

            organization = Organization(
                name=name,
                country=country,
                organization_type=organization_type,
            )

            return repository.create(
                organization
            )

    def get_all(self) -> list[Organization]:

        with get_db() as db:

            repository = OrganizationRepository(db)

            return repository.get_all()

    def get_by_id(
        self,
        organization_id: int,
    ) -> Organization | None:

        with get_db() as db:

            repository = OrganizationRepository(db)

            return repository.get_by_id(
                organization_id
            )

    def search(
        self,
        keyword: str,
    ) -> list[Organization]:

        with get_db() as db:

            repository = OrganizationRepository(db)

            return repository.search(
                keyword.strip()
            )

    def exists(
        self,
        name: str,
    ) -> bool:

        with get_db() as db:

            repository = OrganizationRepository(db)

            return (
                repository.get_by_name(
                    name.strip()
                )
                is not None
            )

    def update(
        self,
        organization: Organization,
    ) -> None:

        with get_db() as db:

            db.merge(organization)
            db.commit()

    def delete(
        self,
        organization_id: int,
    ) -> None:

        with get_db() as db:

            repository = OrganizationRepository(db)

            organization = repository.get_by_id(
                organization_id
            )

            if organization is not None:

                repository.delete(
                    organization
                )