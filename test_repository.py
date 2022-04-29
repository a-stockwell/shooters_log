from time import strftime
import app
import repository
from datetime import date, timedelta

# dates for setting general dates in goals and steps
today = date.today()
evaluation_date = today + timedelta(days=60)
target_date = today + timedelta(days=120)


def test_repository_can_add_athlete(session):
    athlete = app.Athlete("Onename", "lastName", "SS", "GM", None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(athlete)
    session.commit()

    rows = session.execute(
        'SELECT first_name, last_name, current_division, current_classification, add_date FROM "athletes"'
    )
    assert list(rows) == [("Onename", "lastName", "SS", "GM", None)]


def test_repository_can_add_goal(session):
    goal = app.Goal("Draw Time", "Set a part time for draw.", "Short", None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(goal)
    session.commit()

    rows = session.execute(
        'SELECT goal_name, goal_description, goal_term, add_date FROM "goals"'
    )
    assert list(rows) == [
        ("Draw Time", "Set a part time for draw.", "Short", None)]


def test_repository_can_add_step(session):
    # step = app.Step("Master Grip", "Establish a good master grip on the pistol", strftime(
    #     '%Y-%m-%d', today), strftime('%Y-%m-%d', target_date), strftime('%Y-%m-%d', evaluation_date))
    step = app.Step("Master Grip", "Establish master grip on pistol.",
                    step_add_date=None, step_target_date=None, step_evaluation_date=None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(step)
    session.commit()

    rows = session.execute(
        'SELECT step_name, step_description, step_add_date, step_target_date, step_evaluation_date FROM "steps"'
    )
    assert list(rows) == [
        ("Master Grip", "Establish master grip on pistol.", None, None, None)]
