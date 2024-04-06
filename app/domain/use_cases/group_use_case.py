from app.adapters.implementations.group_adapter import GroupAdapter
from app.domain.models.group import Group
from app.infrastructure.repositories.implementations.group_repository import \
    GroupRepository


class GroupUseCase:
    def __init__(self) -> None:
        self.repository = GroupRepository()
        self.adapter = GroupAdapter

    async def list_groups(self):
        group_parsers = []
        groups = await self.repository.read()
        for group in groups:
            group_parsers.append(self.adapter(group[0]).to_model())
        return group_parsers

    async def add_group(self, group: Group):
        try:
            await self.repository.create(self.adapter(group).to_schema())
            return True
        except:
            return False

    async def update_group(self, group: Group):
        try:
            await self.repository.update(self.adapter(group).to_schema())
            return True
        except:
            return False

    async def delete_group(self, id: int):
        try:
            await self.repository.delete(id)
            return True
        except:
            return False
