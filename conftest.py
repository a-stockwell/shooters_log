import imp
import time
from pathlib import Path

import pytest
import requests
from requests.exceptions import ConnectionError
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from config import get_sqlite_file_url

from orm import metadata, start_mappers
import config


def wait_for_webapp_to_come_up():
    deadline = time.time() + 10
    url = config.get_api_url()
    while time.time() < deadline:
        try:
            return requests.get(url)
        except ConnectionError:
            time.sleep(0.5)
    pytest.fail("API never came up")


# @pytest.fixture
# def in_memory_db():
#     engine = create_engine("sqlite:///:memory:")
#     metadata.create_all(engine)
#     return engine


# @pytest.fixture
# def session(in_memory_db):
#     start_mappers()
#     yield sessionmaker(bind=in_memory_db)()
#     clear_mappers()


@pytest.fixture
def file_sqlite_db():
    engine = create_engine(f"sqlite:///shooter_log.db")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(file_sqlite_db):
    start_mappers()
    yield sessionmaker(bind=file_sqlite_db)()
    clear_mappers()


@pytest.fixture
def restart_api():
    (Path(__file__).parent / "flask_app.py").touch()
    time.sleep(0.5)
    wait_for_webapp_to_come_up()
