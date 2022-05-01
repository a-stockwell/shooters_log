from audioop import lin2adpcm
from crypt import methods
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
import app
import orm
import repository
import services

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_sqlite_file_url()))
app = Flask(__name__)


@app.route("/athlete", methods=["POST"])
def athlete_endpoint():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session).list()
    athlete = app.Athlete(
        request.json["athlete_id"], request.json["first_name"], request.json["last_name"], request.json[
            "current_division"], request.json["current_classification"], request.json["add_date"],
    )

    athleteref = app.Athlete()