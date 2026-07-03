"""
Sports Intelligence Platform

File: theme.py
Author: Syed Faran Ali

Description:
Centralized UI theme configuration.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    """Application theme configuration."""

    APP_NAME: str = "Sports Intelligence Platform"

    VERSION: str = "0.2.0"

    PRIMARY_COLOR: str = "#1565C0"

    SECONDARY_COLOR: str = "#1E88E5"

    SUCCESS_COLOR: str = "#2E7D32"

    WARNING_COLOR: str = "#F9A825"

    ERROR_COLOR: str = "#C62828"

    BACKGROUND_COLOR: str = "#F8F9FA"

    SIDEBAR_COLOR: str = "#FFFFFF"

    TEXT_COLOR: str = "#1F2937"

    BORDER_COLOR: str = "#E5E7EB"

    LOGO: str = "🏆"

    COMPANY: str = "Sports Intelligence Platform"


theme = Theme()