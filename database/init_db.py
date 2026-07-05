"""
Database initialization.

Creates all database tables and seeds initial data.
"""

from database.base import Base
from database.session import engine

# Register all SQLAlchemy models
import database.models  # noqa: F401

from database.seed import seed_database


def initialize_database() -> None:
    """
    Initialize the database.

    - Creates all missing tables.
    - Seeds the database only if it has not been seeded.
    """

    # Create tables (safe to call multiple times)
    Base.metadata.create_all(bind=engine)

    # Seed initial data only if required
    seeded = seed_database()

    if seeded:
        print("Database seeded successfully.")
    else:
        print("Database already contains seed data.")

    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()