"""
Database initialization.

Creates all registered SQLAlchemy tables.
"""

from database.base import Base
from database.session import engine

# Register all models
import database.models  # noqa: F401


def initialize_database() -> None:
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)

    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()