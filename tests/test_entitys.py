from app.entities.ticket_model import Ticket
from pytest import mark, fixture
from faker import Faker


@fixture
def fake():
    return Faker()


@mark.ticket_model
def test_ticket_id(fake):
    assert Ticket(id_ticket=fake.random_number(digits=5))


@mark.ticket_model
def test_ticket_link(fake):
    assert Ticket(link=fake.url())


@mark.ticket_model
def test_ticket_description(fake):
    assert Ticket(description=fake.paragraphs(nb=2)[0])
