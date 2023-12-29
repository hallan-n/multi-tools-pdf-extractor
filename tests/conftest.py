from pytest import fixture
from app.db.database import Database
import os


@fixture(scope="session")
def db():
    DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'
    return Database(DB_URL)
