from __future__ import annotations

import app
from app import Athlete
from repository import AbstractRepository


class InvalidAthlete(Exception):
    pass


def is_valid_athlete(athlete, athletes):
    return athlete in {a.athletes for a in athletes}


def athlete(athlete: Athlete, repo: AbstractRepository, session) -> str:
    athletes = repo.list()
    if not is_valid_athlete(athlete.athlete_id, athletes):
        raise InvalidAthlete(f"No Athlete {athlete.athlete_id}")
