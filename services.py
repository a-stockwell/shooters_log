'''
If my understanind is correct we are moving the functions and meathods from the files that they are currently in and into this services file. 
'''
from __future__ import annotations

import app
from app import Athlete
from repository import AbstractRepository, SqlAlchemyRepository


class InvalidAthlete(Exception):
    pass


def is_valid_athlete(athlete, athletes):
    return athlete in {a.athletes for a in athletes}


def add_athlete(athlete: Athlete, repo: AbstractRepository, session) -> str:
    a = repo.add(athlete)


def list_athlete():
    pass
    # Was pulled from the
    # if not is_valid_athlete(athlete.athlete_id, athletes):
    #     raise InvalidAthlete(f"No Athlete {athlete.athlete_id}")
