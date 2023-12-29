from pytest import mark, fixture
from app.db.database import Database
from tests.conftest import db
import os


@mark.database
@mark.skip(reason="Banco de dados rodando em docker")
def test_connection_db(db):
    assert db.is_connect()
