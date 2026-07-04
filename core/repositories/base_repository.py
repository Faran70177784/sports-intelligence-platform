"""
Legacy compatibility module.

Use database.repositories.BaseRepository instead.
"""

from database.repositories.base_repository import BaseRepository

__all__ = [
    "BaseRepository",
]