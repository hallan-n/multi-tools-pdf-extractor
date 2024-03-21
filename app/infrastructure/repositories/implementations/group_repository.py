from app.infrastructure.repositories.interfaces.persistence import Persistence
from app.infrastructure.repositories.config.connection import Connection
from app.infrastructure.schemas.group_schema import Group


class GroupRepository(Persistence):
    def __init__(self):
        self.connection = Connection()

    async def create(self, group: Group):
        """Cria um novo Grupo."""
        try:
            async with self.connection as conn:
                conn.add(group)
                await conn.commit()
        except Exception as e:
            raise RuntimeError(f"Erro ao criar o group: {e}")

    async def read(self):
        from sqlalchemy import select

        """Lê todos os groups."""
        try:
            async with self.connection as conn:
                query = select(Group)
                groups = await conn.execute(query)
                return groups.fetchall()
        except Exception as e:
            raise RuntimeError(f"Erro ao ler os groups: {e}")

    async def update(self, group_new: Group) -> None:
        """Atualiza um group existente."""
        try:
            async with self.connection as conn:
                group = await conn.get(Group, group_new.id)
                if group:
                    group = await conn.merge(group_new)
                    await conn.commit()
                else:
                    raise ValueError("group não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao atualizar o group: {e}")

    async def delete(self, group_del: Group) -> None:
        """Exclui um group."""
        try:
            async with self.connection as conn:
                group = await conn.get(Group, group_del.id)
                if group:
                    await conn.delete(group)
                    await conn.commit()
                else:
                    raise ValueError("group não encontrado")
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir o group: {e}")
