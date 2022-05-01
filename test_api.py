import config
import imp
import pytest

import uuid
import pytest
import requests

import app


def random_suffex():
    return uuid.uuid4().hex[:6]


def random_athlete(name=""):
    # do I need to be returning the entire athlete record?
    return f"athlete-{name}-{random_suffex()}"


@pytest.mark.usefixtures("restart_api")
def test_api_returns_athlete(add_athlete):
    otherathlete = random_athlete
    add_athlete(
        [
            (otherathlete, "other_lname", "SS", "C", "2022-04-29")
        ]
    )
    url = config.get_api_url()

    r = requests.post(f"{url}/athlete", json=add_athlete)
