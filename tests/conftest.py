from pytest import fixture
from faker import Faker
from app.db.database import Database
from app.use_cases.ticket_use_case import TicketUseCases
import os


@fixture(scope="session")
def db():
    DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'
    return Database(DB_URL)


@fixture
def fake():
    return Faker()


@fixture
def ticket_use_cases():
    return TicketUseCases()
