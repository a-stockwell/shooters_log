'''Tests run against the Step class and functions'''

from datetime import date, timedelta
import pytest
from app import Step

# dates for setting general dates in goals and steps
today = date.today()
evaluation_date = today + timedelta(days=60)
target_date = today + timedelta(days=120)


def test_step_info():
    # test thd athlete info display
    test_step01 = Step(
        'Draw Par', 'Set a draw par time and see if it is feasible', today, target_date, evaluation_date)
    test_step01.info()
