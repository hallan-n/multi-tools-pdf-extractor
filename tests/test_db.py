from pytest import mark
from tests.conftest import db


@mark.database
def test_connection_db(db):
    assert db.is_connect() == True
