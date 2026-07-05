"""
Database initialization.

Creates all database tables and seeds initial data.
"""

from database.base import Base
from database.session import engine

# Register all models
import database.models  # noqa: F401

from database.seed import seed_database


def initialize_database() -> None:
    """
    Create all database tables and seed initial data.
    """

    Base.metadata.create_all(bind=engine)

    seed_database()

    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()