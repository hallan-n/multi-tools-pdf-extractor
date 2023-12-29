from pytest import mark
from tests.conftest import ticket_use_cases, fake


@mark.skip(reason="Falta aprimorar")
def test_create_ticket(ticket_use_cases, fake):
    assert (
        ticket_use_cases.create_ticket(
            {
                "id_ticket": fake.pyint(),
                "link": fake.url(),
                "group": fake.name,
                "description": fake.paragraph(),
            },
            rollback=True,
        )
        == True
    )
