"""
Analytics business service.
"""

from database.db import get_db
from database.repositories import (
    EventRepository,
    MatchRepository,
    OrganizationRepository,
    PlayerRepository,
    TeamRepository,
)


class AnalyticsService:
    """Business logic for analytics."""

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    def dashboard_statistics(
        self,
    ) -> dict[str, int]:
        """
        Return dashboard KPI statistics.
        """

        with get_db() as db:

            organization_repository = OrganizationRepository(db)
            team_repository = TeamRepository(db)
            player_repository = PlayerRepository(db)
            match_repository = MatchRepository(db)
            event_repository = EventRepository(db)

            return {
                "organizations": (
                    organization_repository.total_organizations()
                ),
                "teams": (
                    team_repository.total_teams()
                ),
                "players": (
                    player_repository.total_players()
                ),
                "matches": (
                    match_repository.total_matches()
                ),
                "events": (
                    event_repository.total_events()
                ),
            }

    # ---------------------------------------------------------
    # Organization Analytics
    # ---------------------------------------------------------

    def organizations_by_country(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                OrganizationRepository(db)
                .organizations_by_country()
            )

    def teams_per_organization(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                OrganizationRepository(db)
                .teams_per_organization()
            )

    # ---------------------------------------------------------
    # Team Analytics
    # ---------------------------------------------------------

    def teams_by_country(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                TeamRepository(db)
                .teams_by_country()
            )

    def teams_by_organization(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                TeamRepository(db)
                .teams_by_organization()
            )

    def players_per_team(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                TeamRepository(db)
                .players_per_team()
            )

    # ---------------------------------------------------------
    # Player Analytics
    # ---------------------------------------------------------

    def players_by_position(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                PlayerRepository(db)
                .players_by_position()
            )

    def players_by_team(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                PlayerRepository(db)
                .players_by_team()
            )

    # ---------------------------------------------------------
    # Match Analytics
    # ---------------------------------------------------------

    def matches_by_year(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                MatchRepository(db)
                .matches_by_year()
            )

    def matches_by_home_team(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                MatchRepository(db)
                .matches_by_home_team()
            )

    # ---------------------------------------------------------
    # Event Analytics
    # ---------------------------------------------------------

    def events_by_type(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                EventRepository(db)
                .events_by_type()
            )

    def top_scorers(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                EventRepository(db)
                .top_scorers()
            )

    def goals_by_team(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                EventRepository(db)
                .goals_by_team()
            )

    def assists_by_player(
        self,
    ) -> list[tuple]:

        with get_db() as db:

            return (
                EventRepository(db)
                .assists_by_player()
            )