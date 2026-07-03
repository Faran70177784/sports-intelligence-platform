"""
Sports Analytics Dashboard Platform

Application Entry Point
"""

from components.footer import render as render_footer
from components.header import render as render_header
from components.sidebar import render as render_sidebar
from database.database import create_database
from pages.home import render as render_home
from utils.logger import logger


def initialize():
    """
    Initialize the application.
    """

    logger.info("Starting application...")

    create_database()


def main():
    """
    Main application.
    """

    render_header()

    initialize()

    render_sidebar()

    render_home()

    render_footer()


if __name__ == "__main__":
    main()