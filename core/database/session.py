"""
Sports Intelligence Platform

File: session.py
Author: Syed Faran Ali

Description:
Database session factory.
"""

from sqlalchemy.orm import sessionmaker

from core.database.database import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)