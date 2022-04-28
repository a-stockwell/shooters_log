'''Tests run against the athlete class and functions'''

from datetime import date
import pytest
from app import Athlete

today = date.today()


def test_athlete_add():
    # Test adding the athlete to the db
    pass


def test_athlete_delete():
    # test deleteing the athlete from the db
    pass


def test_athlete_info():
    # test thd athlete info display
    test_athlete01 = Athlete(
        'test first name', 'test Last Name', 'SS', 'C', today)
    test_athlete01.info()


def test_athlete_update():
    # Tet changing the athlete in the db
    pass
