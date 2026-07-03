"""
Theme configuration for the Sports Analytics Dashboard Platform.

This module centralizes all UI colors, spacing, and typography
so the application has a consistent professional appearance.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    """Application theme constants."""

    PRIMARY = "#2563EB"
    SECONDARY = "#10B981"
    ACCENT = "#F59E0B"

    SUCCESS = "#22C55E"
    WARNING = "#F59E0B"
    ERROR = "#EF4444"
    INFO = "#0EA5E9"

    BACKGROUND = "#F8FAFC"
    SURFACE = "#FFFFFF"

    TEXT_PRIMARY = "#0F172A"
    TEXT_SECONDARY = "#64748B"

    BORDER = "#E2E8F0"

    BORDER_RADIUS = "12px"

    CARD_PADDING = "20px"

    BOX_SHADOW = "0 2px 10px rgba(0,0,0,0.08)"


theme = Theme()