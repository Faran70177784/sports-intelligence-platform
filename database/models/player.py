"""
Player model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.base import Base
from database.models.audit import AuditMixin


class Player(AuditMixin, Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)

    full_name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    position: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False,
    )

    team = relationship(
        "Team",
        back_populates="players",
    )

    events = relationship(
        "Event",
        back_populates="player",
        cascade="all, delete-orphan",
    )