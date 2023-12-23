from app.entities.ticket_model import Ticket
from pytest import mark
from faker import Faker

fake = Faker()


@mark.ticket_model
def test_ticket_id():
    assert Ticket(id_ticket=fake.random_number(digits=5))


@mark.ticket_model
def test_ticket_link():
    assert Ticket(link=fake.url())


@mark.ticket_model
def test_ticket_description():
    assert Ticket(description=fake.paragraphs(nb=2)[0])
