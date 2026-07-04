"""
database/database.py

Database session management for the Sports Intelligence Platform.
"""

from contextlib import contextmanager
from typing import Generator

from sqlalchemy.orm import Session

from database.session import SessionLocal


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """
    Context manager for database sessions.

    Usage:
        with get_db() as db:
            teams = db.query(Team).all()
    """

    db: Session = SessionLocal()

    try:
        yield db
        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def get_session() -> Session:
    """
    Returns a new database session.

    The caller is responsible for closing the session.

    Example:
        db = get_session()
        try:
            ...
        finally:
            db.close()
    """

    return SessionLocal()