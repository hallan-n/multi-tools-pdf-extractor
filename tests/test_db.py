from pytest import mark
from tests.conftest import db


@mark.skip(reason="Banco rodando em docker")
@mark.database
def test_connection_db(db):
    assert db.is_connect() == True
