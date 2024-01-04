from pytest import mark


@mark.skip(reason="Banco rodando em docker")
@mark.database
def test_connection_db(db):
    assert db.is_connect() == True
