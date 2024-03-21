from app.infrastructure.repositories.interfaces.persistence import Persistence
from app.infrastructure.repositories.config.connection import Connection
from app.infrastructure.schemas.pdf_schema import PDF


class PDFRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    async def create(self, pdf: PDF) -> None:
        """Cria um novo Grupo."""
        try:
            async with self.connection as conn:
                conn.add(pdf)
                await conn.commit()
        except Exception as e:
            raise RuntimeError(f"Erro ao criar o pdf: {e}")

    async def read(self) -> list[PDF]:
        from sqlalchemy import select

        """Lê todos os pdfs."""
        try:
            async with self.connection as conn:
                query = select(PDF)
                pdfs = await conn.execute(query)
                return pdfs.fetchall()
        except Exception as e:
            raise RuntimeError(f"Erro ao ler os pdf: {e}")

    async def update(self, pdf_new: PDF) -> None:
        """Atualiza um pdfexistente."""
        try:
            async with self.connection as conn:
                pdf = await conn.get(PDF, pdf_new.id)
                if pdf:
                    pdf = await conn.merge(pdf_new)
                    await conn.commit()
                else:
                    raise ValueError("pdf não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o pdf: {e}")

    async def delete(self, pdf_del: PDF) -> None:
        """Exclui um pdf"""
        try:
            async with self.connection as conn:
                pdf = await conn.get(PDF, pdf_del.id)
                if pdf:
                    await conn.delete(pdf)
                    await conn.commit()
                else:
                    raise ValueError("pdf não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir o pdf: {e}")
