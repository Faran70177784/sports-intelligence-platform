"""
Application settings.

Loads configuration from environment variables.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file
load_dotenv(BASE_DIR / ".env")


class Settings:
    """Application configuration."""

    APP_NAME = os.getenv("APP_NAME", "Sports Intelligence Platform")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///database/database.db"
    )

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"


settings = Settings()