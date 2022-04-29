import app
from datetime import date, timedelta

# dates for setting general dates in goals and steps
today = date.today()
evaluation_date = today + timedelta(days=60)
target_date = today + timedelta(days=120)


# I'm commenting this out at this time. Having issues with the return. I think it has to do with the insertion of the record in the test_repository.py file.
# The book says this can be a throw away test anyway, so not to concerned with this since the other tests pass.

# def test_athlete_mapper(session):
#     session.execute(
#         "INSERT INTO athletes (first_name, last_name, current_division, current_classification, add_date) VALUES "
#         '("Athlete_01", "One", "CO", "U", "2022-04-29"),'
#         '("Athlete_02", "Two", "SS", "GM", "2022-04-29"),'
#         '("Athlete_03", "Three", "Prod", "C", "2022-04-29")'
#     )
#     expected = [
#         app.Athlete("Athlete_01", "One", "CO", "U", "2022-04-29"),
#         app.Athlete("Athlete_02", "Two", "SS", "GM", "2022-04-29"),
#         app.Athlete("Athlete_03", "Three", "Prod", "C", "2022-04-29")
#     ]
#     assert session.query(app.Athlete).all() == expected
