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
target_date = today + timedelta(days=120)


class Athlete:
    def __init__(self, first_name: str, last_name: str, current_division: str, current_classification: str, add_date: Optional[date]):
        # init for the athlete
        # self.athlete_id = athlete_id
        self.first_name = first_name
        self.last_name = last_name
        self.current_division = current_division
        self.current_classification = current_classification
        self.add_date = add_date

    def add(self):
        # used to add the athlete information to the DB
        pass

    def delete(self):
        # used to delete the athlete information in the DB
        pass

    def info(self):
        # used to display the athlete's information
        try:
            return(f'First Name: {self.first_name}\nLast Name: {self.last_name}\nCurrent Division and Class: {self.current_division} {self.current_classification}')
        except StopIteration:
            raise NoAthlete(f'No athlete found with provided name')

#   pulling out of the project
    # def update(self):
    #     # used to update the athlete information in the DB
    #     pass


class Run:
    def __init__(self, athlete_id: int, raw_time: float, mikes: int, penalties: int, add_date: Optional[date]):
        self.athlete_id = athlete_id
        self.raw_time = raw_time
        self.mikes = mikes
        self.penalties = penalties
        self.add_date = add_date

    def add(self):
        # used to add the athlete information to the DB
        pass

    def delete(self):
        # used to delete the athlete information in the DB
        pass

    def info(self):
        return(f'Run Information\nathlete_id: {self.athlete_id}\nraw_time: {self.raw_time}\nmikes: {self.mikes}\npenalites: {self.penalties}\nadd_date: {self.add_date}')


# class Goal:
#     # used to create the Goal piece of the system
#     def __init__(self, goal_name: str, goal_description: str, goal_term: str, add_date: Optional[date]):
#         self.goal_name = goal_name
#         self.goal_description = goal_description
#         self.goal_term = goal_term
#         self.add_date = add_date

#     def info(self):
#         return(f'Goal Information\nName: {self.goal_name}\nDescription: {self.goal_description}\nTerm: {self.goal_term}')


class NoAthlete(Exception):
    # Exception for no found athlete
    pass


# class Step:
#     # Step information for the system
#     def __init__(self, step_name: str, step_description: str, step_add_date: Optional[date], step_target_date: Optional[date], step_evaluation_date: Optional[date]):
#         self.step_name = step_name
#         self.step_description = step_description
#         self.step_add_date = step_add_date
#         self.step_target_date = step_target_date
#         self.step_evaluation_date = step_evaluation_date

#     def info(self):
#         return(f'Step Information\nName: {self.step_name}\nDescription: {self.step_description}\nDate Added: {self.step_add_date}')


def athlete() -> str:
    try:
        pass
    except StopIteration:
        raise NoAthlete(f"No Athlete by the provided name")
