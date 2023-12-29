from pytest import mark
from tests.conftest import db


@mark.database
def test_connection_db(db):
    assert db.is_connect() == True


@mark.database
def test_create_tables(db):
    assert db.create_tables(rollback=True) == True
