'''
This is the first milestone and task section is for the CIDM 6330 Spring 2022 final project.

Working on following along with the book 'Architecture Patters with Python' by Harry J.W. Percival & Bob Gregory. 

This first milestone and task section is an attempt to follow along and create chapter 1 with against my problem. 

My problem is a Shooters Log for tracking training goals and performance improvements. This is further expanded on in the project workup. 

This first step is done, I think. Have created three classes inside the domain area. Created corresponding tests for each Info display part. Those are passing at this time with the created tests. I have added the DB methods to the Athlete class, but will need to add the DB methods to the Goal and Step classes. 
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional, List, Set

# dates for setting general dates in goals and steps
today = date.today()
evaluation_date = today + timedelta(days=60)
targe_date = today + timedelta(days=120)


class Athlete:
    def __init__(self, first_name: str, last_name: str, current_division: str, current_classification: str, add_date: Optional[date]):
        # init for the athlete
        self.first_name = first_name
        self.last_name = last_name
        self.current_division = current_division
        self.current_classification = current_classification

    def athlete_add(self):
        # used to add the athlete information to the DB
        pass

    def athlete_delete(self):
        # used to delete the athlete information in the DB
        pass

    def athlete_info(self):
        # used to display the athlete's information
        try:
            return(f'First Name: {self.first_name}\nLast Name: {self.last_name}\nCurrent Division and Class: {self.current_division} {self.current_classification}')
        except StopIteration:
            raise NoAthlete(f'No athlete found with provided name')

    def athlete_update(self):
        # used to update the athlete information in the DB
        pass


class Goal:
    # used to create the Goal piece of the system
    def __init__(self, goal_name: str, goal_description: str, goal_term: str):
        self.goal_name = goal_name
        self.goal_description = goal_description
        self.goal_term = goal_term

    def goal_info(self):
        return(f'Goal Information\nName: {self.goal_name}\nDescription: {self.goal_description}\nTerm: {self.goal_term}')


class NoAthlete(Exception):
    # Exception for no found athlete
    pass


class Step:
    # Step information for the system
    # used to create the Goal piece of the system
    def __init__(self, step_name: str, step_description: str, step_add_date: date):
        self.step_name = step_name
        self.step_description = step_description
        self.step_add_date = step_add_date

    def step_info(self):
        return(f'Step Information\nName: {self.step_name}\nDescription: {self.step_description}\nDate Added: {self.step_add_date}')


# athlete_01 = Athlete('Andy', 'Stockwell', 'SS', 'UN', today)
# athlete_02 = Athlete('Nando', 'Roca', 'CO', 'C', today)

# print(athlete_01.athlete_info())
# print(athlete_02.athlete_info())
