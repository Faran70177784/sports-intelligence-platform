"""
Compatibility layer for the legacy core.database package.

This module forwards database initialization and session access
to the new enterprise database package.
"""

from database.init_db import initialize_database
from database.session import SessionLocal
from database.session import engine
from database.base import Base

__all__ = [
    "initialize_database",
    "SessionLocal",
    "engine",
    "Base",
]