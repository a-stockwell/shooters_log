'''Test the new "Runs" class'''

from datetime import date
import pytest
from app import Run

today = date.today()


def test_run_add():
    # Test adding the run to the db
    pass


def test_run_delete():
    # test deleteing the run from the db
    pass


def test_run_info():
    # test the run info display
    test_run01 = Run(1, 38.46, 0, 2, '2022-05-01')
    test_run01.info()


def test_run_update():
    # Tet changing the run in the db
    pass
