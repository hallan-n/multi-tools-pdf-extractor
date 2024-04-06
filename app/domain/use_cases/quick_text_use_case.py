from app.adapters.implementations.quick_text_adapter import QuickTextAdapter
from app.domain.models.group import Group
from app.domain.models.quick_text import QuickText
from app.infrastructure.repositories.implementations.group_repository import \
    GroupRepository
from app.infrastructure.repositories.implementations.quick_text_repository import \
    QuickTextRepository


class QuickTextUseCase:
    def __init__(self) -> None:
        self.text_repository = QuickTextRepository()
        self.group_repository = GroupRepository()
        self.adapter = QuickTextAdapter

    async def add_text(self, text: QuickText):
        try:
            await self.text_repository.create(self.adapter(text).to_schema())
            return True
        except:
            return False

    async def get_all_texts(self):
        texts_parsers = []
        texts = await self.text_repository.read()
        for text in texts:
            texts_parsers.append(self.adapter(text[0]).to_model())
        return texts_parsers

    async def update_text(self, quick_text: QuickText):
        try:
            await self.text_repository.update(quick_text)
            return True
        except:
            return False

    async def delete_text(self, id: int):
        try:
            await self.text_repository.delete(id)
            return True
        except:
            return False

    async def add_group(self, quick_text_id: int, group: Group):
        try:
            group.quick_text_id = quick_text_id
            await self.group_repository.create(group)
            return True
        except:
            return False
