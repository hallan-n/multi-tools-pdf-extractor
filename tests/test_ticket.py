from pytest import mark
from app.entities.schemas.ticket_schema import Ticket


@mark.skip(reason="Banco rodando em docker")
def test_create_ticket(ticket_use_cases):
    assert (
        ticket_use_cases.create_ticket(
            Ticket(
                id_ticket=1,
                link="https://www.teste.com.br",
                group="teste",
                description="texto teste",
                create_at="2000-10-10",
            ),
            rollback=True,
        )
        == True
    )


@mark.skip(reason="Banco rodando em docker")
def test_select_tickets(ticket_use_cases):
    assert ticket_use_cases.select_tickets(page=1, page_size=1, tests=True) == True
