"""
Sports Intelligence Platform

File: initialize.py
Author: Syed Faran Ali

Description:
Database initialization.
"""

from core.database.base import Base
from core.database.database import engine

# Import models here so SQLAlchemy registers them
from core.database.models import *  # noqa: F401,F403


def initialize_database() -> None:
    """
    Create database tables.
    """

    Base.metadata.create_all(bind=engine)