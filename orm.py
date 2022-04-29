from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, column
from sqlalchemy.orm import mapper, relationship

import app

metadata = MetaData()

athletes = Table(
    "athletes",
    metadata,
    Column("athlete_id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(25)),
    Column("last_name", String(25)),
    Column("current_division", String(4)),
    Column("current_classification", String(2)),
    Column("add_date", Date, nullable=True),
)

goals = Table(
    "goals",
    metadata,
    Column("goal_id", Integer, primary_key=True, autoincrement=True),
    Column("goal_name", String(30)),
    Column("goal_description", String(255)),
    Column("goal_term", String(5)),
    Column("add_date", Date, nullable=True),
)

steps = Table(
    "steps",
    metadata,
    Column("step_id", Integer, primary_key=True, autoincrement=True),
    Column("step_name", String(30)),
    Column("step_description", String(255)),
    Column("step_add_date", Date, nullable=True),
    Column("step_target_date", Date, nullable=True),
    Column("step_evaluation_date", Date, nullable=True),
)


def start_mappers():
    lines_mapper = mapper(app.Athlete, athletes)
    lines_mapper = mapper(app.Goal, goals)
    lines_mapper = mapper(app.Step, steps)
