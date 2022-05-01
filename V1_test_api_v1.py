from cmath import atanh
import uuid
import pytest
import requests

import config


def random_suffex():
    return uuid.uuid4().hex[:6]


def random_athlete(name=""):
    return f"athlete-{name}-{random_suffex()}"


def random_goal(name=""):
    return f"goal-{name}-{random_suffex()}"


def random_step(name=""):
    return f"step-{name}-{random_suffex()}"


@pytest.mark.usefixtures("restart_api")
    # what needs to go in the function for my stuff? athlete?
def test_happy_path_returns_201_and_athlete_info(add_athlete):
    other_athlete = random_athlete("other")
    other_goal = random_goal("other")
    other_step = random_step("other")
    add_athlete(
        [
            (other_athlete, "")
        ]
    )
