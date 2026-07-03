"""
Configuration module for the Sports Analytics Dashboard Platform.

This module loads and validates all application settings from the .env
file using Pydantic Settings.

Author: Syed Faran Ali
Project: Sports Analytics Dashboard Platform
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ==================================================
    # Application
    # ==================================================
    app_name: str = Field(..., alias="APP_NAME")
    app_version: str = Field(..., alias="APP_VERSION")
    app_env: str = Field(..., alias="APP_ENV")
    debug: bool = Field(default=False, alias="DEBUG")

    # ==================================================
    # Database
    # ==================================================
    database_url: str = Field(..., alias="DATABASE_URL")

    # ==================================================
    # Logging
    # ==================================================
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    # ==================================================
    # Directories
    # ==================================================
    upload_dir: str = Field(..., alias="UPLOAD_DIR")
    export_dir: str = Field(..., alias="EXPORT_DIR")
    assets_dir: str = Field(..., alias="ASSETS_DIR")

    # ==================================================
    # Theme
    # ==================================================
    primary_color: str = Field(..., alias="PRIMARY_COLOR")
    secondary_color: str = Field(..., alias="SECONDARY_COLOR")
    accent_color: str = Field(..., alias="ACCENT_COLOR")


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.

    Returns:
        Settings: Application configuration.
    """
    return Settings()


settings = get_settings()