from app.adapters.implementations.ticket_adapter import TicketAdapter
from app.domain.models.ticket import Ticket
from app.infrastructure.repositories.implementations.ticket_repository import \
    TicketRepository


class TicketUseCase:
    def __init__(self) -> None:
        self.repository = TicketRepository()
        self.adapter = TicketAdapter

    async def list_tickets(self):
        ticket_parsers = []
        tickets = await self.repository.read()
        for ticket in tickets:
            ticket_parsers.append(self.adapter(ticket[0]).to_model())
        return ticket_parsers

    async def add_ticket(self, ticket: Ticket):
        try:
            await self.repository.create(self.adapter(ticket).to_schema())
            return True
        except:
            return False

    async def update_ticket(self, ticket: Ticket):
        try:
            await self.repository.update(self.adapter(ticket).to_schema())
            return True
        except:
            return False

    async def delete_ticket(self, id: int):
        try:
            await self.repository.delete(id)
            return True
        except:
            return False
