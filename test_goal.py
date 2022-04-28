'''Tests run against the Goal class and functions'''

from datetime import date
import pytest
from app import Goal

today = date.today()


def test_goal_info():
    # test thd athlete info display
    test_goal01 = Goal(
        'Improve Draw', 'Working to improve draw time from the holster', 'short')
    test_goal01.info()
