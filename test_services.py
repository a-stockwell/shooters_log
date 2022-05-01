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
import random

from datetime import date

# dates for setting general usage
today = date.today()
# random value for raw time insert
raw_time_rand = round(random.uniform(1, 50), 2)
mikes_rand = random.randint(0, 6)
penalties_rand = random.randint(0, 25)


def test_add_athlete(session):
    test_athlete = app.Athlete("robert", "lathem", "SS", "GM", today)
    # repo = FakeRepository([athlete])
    # repo = repository.SqlAlchemyRepository(test_athlete)
    repo = repository.SqlAlchemyRepository([test_athlete])
    result = services.add_athlete(test_athlete)


def test_add_run(session):
    testrun = app.Run(1, raw_time_rand, mikes_rand, penalties_rand, today)
    repo = repository.SqlAlchemyRepositoryRun(testrun)
    result = services.add_run()

# Not sure this one is needed in my project, followed from the book.
# def test_commits():
#     '''Need to add the Goal and Step test as well'''
#     athlete = app.Athlete("travis", "tomosi", "Lim", "M", today)
#     repo = FakeRepository([athlete])
#     session = FakeSession()

#     services.athlete(athlete, repo, session)
#     assert session.committed is True

# Not doing the fake repository, doing test directely into the shooter_log.db
# class FakeRepository(repository.AbstractRepository):
#     def __init__(self, athletes):
#         self._athletes = set(athletes)

#     def add(self, batch):
#         self._athletes.add(athlete)

#     def get(self, reference) -> app.Athlete:
#         return next(a for a in self._athletes if a.reference == reference)

#     def list(self):
#         return list(self._athletes)


# class FakeSession:
#     committed = False

#     def commit(self):
#         self.committed = True
