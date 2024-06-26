from sqlalchemy import select

from app.infrastructure.repositories.config.connection import Connection
from app.infrastructure.repositories.interfaces.persistence import Persistence
from app.infrastructure.schemas.ticket_schema import Ticket


class TicketRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    async def create(self, ticket: Ticket) -> None:
        """Cria um novo ticket."""
        try:
            async with self.connection as conn:
                conn.add(ticket)
                await conn.commit()
        except Exception as e:
            raise RuntimeError(f"Erro ao criar o ticket: {e}")

    async def read(self) -> list[Ticket]:
        """Lê todos os tickets."""
        try:
            async with self.connection as conn:
                query = select(Ticket)
                tickets = await conn.execute(query)
                return tickets.fetchall()
        except Exception as e:
            raise RuntimeError(f"Erro ao ler os tickets: {e}")

    async def update(self, ticket_new: Ticket) -> None:
        """Atualiza um ticket existente."""
        try:
            async with self.connection as conn:
                ticket = await conn.get(Ticket, ticket_new.id)
                if ticket:
                    ticket = await conn.merge(ticket_new)
                    await conn.commit()
                else:
                    raise ValueError("ticket não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o ticket: {e}")

    async def delete(self, ticket_id: int) -> None:
        """Exclui um ticket."""
        try:
            async with self.connection as conn:
                ticket = await conn.get(Ticket, ticket_id)
                if ticket:
                    await conn.delete(ticket)
                    await conn.commit()
                else:
                    raise ValueError("ticket não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir o ticket: {e}")
