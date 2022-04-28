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

    rows = session.execute(
        'SELECT first_name, last_name, current_division, current_classification, add_date FROM "athletes"'
    )
    assert list(rows) == [("Onename", "lastName", "SS", "GM", today)]
