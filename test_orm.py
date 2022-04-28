import app
from datetime import date

# throw away tests


def test_athlete_mapper(session):
    session.execute(
        "INSERT INTO athletes (first_name, last_name, current_division, current_classification) VALUES "
        '("Athlete_01", "One", "CO", "U"),'
        '("Athlete_02", "Two", "SS", "GM"),'
        '("Athlete_03", "Three", "Prod", "C")'
    )
    expected = [
        app.Athlete("Athlete_01", "One", "CO", "U"),
        app.Athlete("Athlete_02", "Two", "SS", "GM"),
        app.Athlete("Athlete_03", "Three", "Prod", "C")
    ]
    assert session.query(app.Athlete).all() == expected