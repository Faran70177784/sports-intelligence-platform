"""
Database seeding script.

Creates initial application data.
Safe to run multiple times (idempotent).
"""

from datetime import date

from auth.security import SecurityManager
from database.db import get_db
from database.models import (
    Event,
    Match,
    Player,
    Team,
    User,
)


def seed_database() -> None:
    """
    Seed the database with initial data.
    """

    security = SecurityManager()

    with get_db() as db:

        # ==========================================================
        # Administrator
        # ==========================================================
        admin = (
            db.query(User)
            .filter(User.username == "admin")
            .first()
        )

        if admin is None:
            admin = User(
                username="admin",
                password=security.hash_password("admin123"),
                role="Administrator",
            )

            db.add(admin)

        # ==========================================================
        # Teams
        # ==========================================================
        team_data = [
            ("Manchester City", "England"),
            ("Liverpool", "England"),
            ("Barcelona", "Spain"),
            ("Real Madrid", "Spain"),
        ]

        teams = {}

        for name, country in team_data:

            team = (
                db.query(Team)
                .filter(Team.name == name)
                .first()
            )

            if team is None:
                team = Team(
                    name=name,
                    country=country,
                )
                db.add(team)
                db.flush()

            teams[name] = team

        # ==========================================================
        # Players
        # ==========================================================
        player_data = [

            ("Erling Haaland", "Forward", "Manchester City"),
            ("Kevin De Bruyne", "Midfielder", "Manchester City"),
            ("Mohamed Salah", "Forward", "Liverpool"),
            ("Virgil van Dijk", "Defender", "Liverpool"),
            ("Robert Lewandowski", "Forward", "Barcelona"),
            ("Pedri", "Midfielder", "Barcelona"),
            ("Jude Bellingham", "Midfielder", "Real Madrid"),
            ("Vinicius Junior", "Forward", "Real Madrid"),

        ]

        players = {}

        for full_name, position, team_name in player_data:

            player = (
                db.query(Player)
                .filter(Player.full_name == full_name)
                .first()
            )

            if player is None:
                player = Player(
                    full_name=full_name,
                    position=position,
                    team=teams[team_name],
                )

                db.add(player)
                db.flush()

            players[full_name] = player

        # ==========================================================
        # Match
        # ==========================================================
        match = db.query(Match).first()

        if match is None:

            match = Match(
                home_team=teams["Manchester City"].id,
                away_team=teams["Liverpool"].id,
                match_date=date.today(),
            )

            db.add(match)
            db.flush()

        # ==========================================================
        # Match Events
        # ==========================================================
        if db.query(Event).count() == 0:

            events = [

                Event(
                    match=match,
                    player=players["Erling Haaland"],
                    minute=12,
                    event_type="Goal",
                ),

                Event(
                    match=match,
                    player=players["Mohamed Salah"],
                    minute=39,
                    event_type="Goal",
                ),

                Event(
                    match=match,
                    player=players["Kevin De Bruyne"],
                    minute=72,
                    event_type="Assist",
                ),

            ]

            db.add_all(events)

    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_database()