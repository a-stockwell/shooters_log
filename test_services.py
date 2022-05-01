'''
Test for the Services.py file.

This should move the tests from the domain level to the services level in the pattern.

So the test_athlete and test_runs should live here now, if my understanding is correct. This is a combination of chapter 4 and 5. 
'''
from unittest import result

from requests import session
import app
import pytest
import repository
import services


class FakeRepository(repository.AbstractRepository):
    def __init__(self, athletes):
        self._athletes = set(athletes)

    def add(self, batch):
        self._athletes.add(athlete)

    def get(self, reference) -> app.Athlete:
        return next(a for a in self._athletes if a.reference == reference)

    def list(self):
        return list(self._athletes)


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_returns_athlete():
    athlete = app.Athlete("bob", "lathem", "SS", "GM", "2022-04-29")
    repo = FakeRepository([athlete])

    result = services.is_athlete()


def test_commits():
    '''Need to add the Goal and Step test as well'''
    athlete = app.Athlete("travis", "tomosi", "Lim", "M", "2022-04-29")
    repo = FakeRepository([athlete])
    session = FakeSession()

    services.athlete(athlete, repo, session)
    assert session.committed is True
