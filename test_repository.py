import re
from time import strftime
import app
import repository
from datetime import date, timedelta

# dates for setting general dates in goals and steps
today = date.today()
evaluation_date = today + timedelta(days=60)
target_date = today + timedelta(days=120)


def test_repository_can_add_athlete(session):
    athlete = app.Athlete("Onename", "lastName", "SS", "GM", today)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(athlete)
    session.commit()

    # print(athlete.info())

    # Use Get method to grab the latest athlete that was created just above.
    # Stores into another object so they can be compaired.
    athlete2 = repo.get(athlete)
    # print(athlete2.info())

    assert athlete == athlete2  # compare the two.

    # rows = session.execute(
    #     'SELECT first_name, last_name, current_division, current_classification, add_date FROM "athletes"'
    # )
    # print(list(rows))
    # assert list(rows) == [("Onename", "lastName", "SS", "GM", None)]


def test_repository_can_add_run(session):
    # following the pattern above should return the info in the same way.
    run = app.Run(1, 33.42, 0, 2, today)

    repo = repository.SqlAlchemyRepositoryRun(session)
    repo.add(run)
    session.commit()

    run2 = repo.get(run)

    assert run == run2


# -------- Goals and Steps info commented out below --------
# Commenting out the Goal part of the Repository test
# def test_repository_can_add_goal(session):
#     goal = app.Goal("Draw Time", "Set a part time for draw.", "Short", None)

#     repo = repository.SqlAlchemyRepository(session)
#     repo.add(goal)
#     session.commit()

#     rows = session.execute(
#         'SELECT goal_name, goal_description, goal_term, add_date FROM "goals"'
#     )
#     assert list(rows) == [
#         ("Draw Time", "Set a part time for draw.", "Short", None)]

# Commenting out the Step part of the repository test.
# def test_repository_can_add_step(session):
#     # step = app.Step("Master Grip", "Establish a good master grip on the pistol", strftime(
#     #     '%Y-%m-%d', today), strftime('%Y-%m-%d', target_date), strftime('%Y-%m-%d', evaluation_date))
#     step = app.Step("Master Grip", "Establish master grip on pistol.",
#                     step_add_date=None, step_target_date=None, step_evaluation_date=None)

#     repo = repository.SqlAlchemyRepository(session)
#     repo.add(step)
#     session.commit()

#     rows = session.execute(
#         'SELECT step_name, step_description, step_add_date, step_target_date, step_evaluation_date FROM "steps"'
#     )
#     assert list(rows) == [
#         ("Master Grip", "Establish master grip on pistol.", None, None, None)]
