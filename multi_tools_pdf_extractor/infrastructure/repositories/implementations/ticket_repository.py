from multi_tools_pdf_extractor.infrastructure.repositories.interfaces.persistence import (
    Persistence,
)
from multi_tools_pdf_extractor.infrastructure.repositories.config.connection import (
    Connection,
)
from multi_tools_pdf_extractor.infrastructure.schemas.ticket_schema import Ticket


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

    async def read(self):
        """Lê todos os tickets."""
        try:
            async with self.connection as conn:
                tickets = await conn.execute(conn.query(Ticket))
                return tickets.fetchall()
        except Exception as e:
            raise RuntimeError(f"Erro ao ler os tickets: {e}")

    async def update(self, ticket_new: Ticket) -> None:
        """Atualiza um ticket existente."""
        try:
            async with self.connection as conn:
                ticket = await conn.get(Ticket, ticket_new.id)
                if ticket:
                    ticket = conn.merge(ticket_new)
                    await conn.commit()
                else:
                    raise ValueError("Ticket não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o ticket: {e}")

    async def delete(self, ticket_del: Ticket) -> None:
        """Exclui um ticket."""
        try:
            async with self.connection as conn:
                ticket = await conn.get(Ticket, ticket_del.id)
                if ticket:
                    conn.delete(ticket)
                    await conn.commit()
                else:
                    raise ValueError("Ticket não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir o ticket: {e}")
