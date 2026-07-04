"""
Initialize all database tables.
"""

from database.base import Base
from database.session import engine

# Register all SQLAlchemy models
from database.models import Event
from database.models import Match
from database.models import Player
from database.models import Team
from database.models import User


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()