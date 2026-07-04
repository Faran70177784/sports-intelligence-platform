"""
Match model.
"""

from datetime import date

from sqlalchemy import Date
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.base import Base
from database.models.audit import AuditMixin


class Match(AuditMixin, Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)

    home_team: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False,
    )

    away_team: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False,
    )

    match_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    events = relationship(
        "Event",
        back_populates="match",
        cascade="all, delete-orphan",
    )