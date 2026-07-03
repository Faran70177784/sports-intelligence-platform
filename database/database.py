"""
Database configuration for the Sports Analytics Dashboard Platform.

This module creates the SQLAlchemy engine, session factory,
and declarative base.

Author: Syed Faran Ali
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from config import settings
from utils.logger import logger


class Base(DeclarativeBase):
    """
    Base class for all ORM models.
    """
    pass


logger.info("Initializing database engine...")

engine = create_engine(
    settings.database_url,
    echo=settings.debug,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db():
    """
    Creates a database session.

    Yields:
        Session
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def create_database():
    """
    Creates all database tables.
    """

    logger.info("Creating database tables...")

    Base.metadata.create_all(bind=engine)

    logger.success("Database initialized successfully.")