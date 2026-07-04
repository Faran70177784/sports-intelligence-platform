"""
Compatibility layer for legacy repository imports.

The enterprise repository implementation now lives in
database.repositories.
"""

from database.repositories import (
    BaseRepository,
    TeamRepository,
    UserRepository,
)

__all__ = [
    "BaseRepository",
    "TeamRepository",
    "UserRepository",
]