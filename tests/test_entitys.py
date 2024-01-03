from app.entities.schemas.ticket_schema import Ticket
from tests.conftest import fake
from pytest import mark


@mark.ticket_schema
def test_ticket_id(fake):
    assert Ticket(id_ticket=fake.random_number(digits=5))


@mark.ticket_schema
def test_ticket_link(fake):
    assert Ticket(link=fake.url())


@mark.ticket_schema
def test_ticket_description(fake):
    assert Ticket(description=fake.paragraphs(nb=2)[0])
