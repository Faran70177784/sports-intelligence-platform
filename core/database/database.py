"""
Sports Intelligence Platform

File: database.py
Author: Syed Faran Ali

Description:
Database engine configuration.
"""

from pathlib import Path

from sqlalchemy import create_engine

DATABASE_PATH = Path("database/app.db")

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)