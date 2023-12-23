from app.entity.ticket import Ticket
from pytest import mark
from faker import Faker

fake = Faker()


@mark.ticket
def test_ticket_id():
    assert Ticket(id=fake.random_number(digits=5))


@mark.ticket
def test_ticket_author():
    assert Ticket(author=fake.random_number(digits=5))


@mark.ticket
def test_ticket_description():
    assert Ticket(description=fake.paragraphs(nb=1)[0])
