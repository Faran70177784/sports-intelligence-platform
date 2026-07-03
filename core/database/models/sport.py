"""
Sports Intelligence Platform

File: sport.py
Author: Syed Faran Ali

Description:
Sport database model.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.database.base import Base


class Sport(Base):
    """
    Sport model.
    """

    __tablename__ = "sports"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    category: Mapped[str] = mapped_column(
        String(100)
    )