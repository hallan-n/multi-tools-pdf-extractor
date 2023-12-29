from pytest import mark
from app.entities.ticket_model import Ticket
from app.entities.ticket_sql import TicketSQL
from tests.conftest import ticket_use_cases


def test_create_ticket(ticket_use_cases):
    assert (
        ticket_use_cases.create_ticket(
            Ticket(
                id_ticket=1,
                link="https://www.teste.com.br",
                group="teste",
                description="texto teste",
            ),
            rollback=True,
        )
        == True
    )


def test_select_tickets(ticket_use_cases):
    assert ticket_use_cases.select_tickets(page=1, page_size=1, tests=True) == True
