from sqlalchemy import select

from app.infrastructure.repositories.config.connection import Connection
from app.infrastructure.repositories.interfaces.persistence import Persistence
from app.infrastructure.schemas.quick_text_schema import QuickText


class QuickTextRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    async def create(self, quick_text: QuickText) -> None:
        """Cria um novo QuickText."""
        try:
            async with self.connection as conn:
                conn.add(quick_text)
                await conn.commit()
        except Exception as e:
            raise RuntimeError(f"Erro ao criar o quick_text: {e}")

    async def read(self) -> list[QuickText]:
        """Lê todos os QuickTexts."""
        try:
            async with self.connection as conn:
                query = select(QuickText)
                quick_texts = await conn.execute(query)
                return quick_texts.fetchall()
        except Exception as e:
            raise RuntimeError(f"Erro ao ler os QuickTexts: {e}")

    async def update(self, quick_text_new: QuickText) -> None:
        """Atualiza um QuickText existente."""
        try:
            async with self.connection as conn:
                quick_text = await conn.get(QuickText, quick_text_new.id)
                if quick_text:
                    quick_text = await conn.merge(quick_text_new)
                    await conn.commit()
                else:
                    raise ValueError("QuickText não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o quick_text: {e}")

    async def delete(self, id: int) -> None:
        """Exclui um QuickText."""
        try:
            async with self.connection as conn:
                quick_text = await conn.get(QuickText, id)
                if quick_text:
                    await conn.delete(quick_text)
                    await conn.commit()
                else:
                    raise ValueError("QuickText não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir o quick_text: {e}")
