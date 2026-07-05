"""
Organization model.

Represents a sports organization such as a club,
federation, league, university, academy, or association.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.base import Base
from database.models.audit import AuditMixin


class Organization(AuditMixin, Base):
    """Sports organization."""

    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    organization_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    teams = relationship(
        "Team",
        back_populates="organization",
        cascade="all, delete-orphan",
    )