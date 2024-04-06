from sqlalchemy import select

from app.infrastructure.repositories.config.connection import Connection
from app.infrastructure.repositories.interfaces.persistence import Persistence
from app.infrastructure.schemas.brokerage_schema import Brokerage


class BrokerageRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    async def create(self, brokerage: Brokerage) -> None:
        """Cria um novo Brokerage."""
        try:
            async with self.connection as conn:
                conn.add(brokerage)
                await conn.commit()
        except Exception as e:
            raise RuntimeError(f"Erro ao criar o brokerage: {e}")

    async def read(self) -> list[Brokerage]:
        """Lê todos os BrokerageS."""
        try:
            async with self.connection as conn:
                query = select(Brokerage)
                brokerages = await conn.execute(query)
                return brokerages.fetchall()
        except Exception as e:
            raise RuntimeError(f"Erro ao ler os Brokerage: {e}")

    async def update(self, brokerage_new: Brokerage) -> None:
        """Atualiza um Brokerage existente."""
        try:
            async with self.connection as conn:
                brokerage = await conn.get(Brokerage, brokerage_new.id)
                if brokerage:
                    brokerage = await conn.merge(brokerage_new)
                    await conn.commit()
                else:
                    raise ValueError("Brokerage não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o Brokerage: {e}")

    async def delete(self, brokerage_del: Brokerage) -> None:
        """Exclui um QuickText."""
        try:
            async with self.connection as conn:
                brokerage = await conn.get(Brokerage, brokerage_del.id)
                if brokerage:
                    await conn.delete(brokerage)
                    await conn.commit()
                else:
                    raise ValueError("Brokerage não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir o Brokerage: {e}")
