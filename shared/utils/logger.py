"""
Professional logging configuration for the Sports Analytics Dashboard Platform.

Author: Syed Faran Ali
"""

from pathlib import Path
import sys

from loguru import logger

from config import settings

# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Remove Loguru's default logger
logger.remove()

# Console logging
logger.add(
    sys.stdout,
    level=settings.log_level,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
    colorize=True,
)

# File logging with automatic rotation
logger.add(
    LOG_DIR / "application.log",
    level=settings.log_level,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    encoding="utf-8",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level:<8} | "
        "{name}:{function}:{line} | "
        "{message}"
    ),
)

__all__ = ["logger"]