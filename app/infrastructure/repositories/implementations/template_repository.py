from sqlalchemy import select

from app.infrastructure.repositories.config.connection import Connection
from app.infrastructure.repositories.interfaces.persistence import Persistence
from app.infrastructure.schemas.template_schema import Template


class TemplateRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    async def create(self, template: Template) -> None:
        """Cria um novo template."""
        try:
            async with self.connection as conn:
                conn.add(template)
                await conn.commit()
        except Exception as e:
            raise RuntimeError(f"Erro ao criar o template: {e}")

    async def read(self) -> list[Template]:
        """Lê todos os templates."""
        try:
            async with self.connection as conn:
                query = select(Template)
                templates = await conn.execute(query)
                return templates.fetchall()
        except Exception as e:
            raise RuntimeError(f"Erro ao ler os templates: {e}")

    async def update(self, template_new: Template) -> None:
        """Atualiza um template existente."""
        try:
            async with self.connection as conn:
                template = await conn.get(Template, template_new.id)
                if template:
                    template = await conn.merge(template_new)
                    await conn.commit()
                else:
                    raise ValueError("template não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o template: {e}")

    async def delete(self, template_del: Template) -> None:
        """Exclui um template."""
        try:
            async with self.connection as conn:
                template = await conn.get(Template, template_del.id)
                if template:
                    await conn.delete(template)
                    await conn.commit()
                else:
                    raise ValueError("template não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir o template: {e}")
