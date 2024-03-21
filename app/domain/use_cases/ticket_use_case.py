from domain.models.group import Group
from domain.models.ticket import Ticket
from infrastructure.repositories.implementations.ticket_repository import (
    TicketRepository,
)


class TicketUseCase:
    def __init__(self) -> None:
        self.repository = TicketRepository()

    def list_tickets(self):
        ...

    def add_ticket(self, ticket: Ticket):
        ...

    def add_group(self, ticket: Ticket, group: Group):
        ...
