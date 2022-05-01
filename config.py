import os


def get_sqlite_file_url():
    '''
    Continue using the SQLite DB for the project.
    '''
    return f"sqlite:///shooter_log.db"


def get_postres_uri():
    '''
    Adding this just to follow along with the book
    '''
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "abc123")
    user, db_name = 'allocation', 'allocation'
    return f"postresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    '''
    Creating the API hook
    '''
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"
