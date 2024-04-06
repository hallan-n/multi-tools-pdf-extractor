from app.adapters.implementations.quick_text_adapter import QuickTextAdapter
from app.domain.models.quick_text import QuickText
from app.infrastructure.repositories.implementations.quick_text_repository import \
    QuickTextRepository


class QuickTextUseCase:
    def __init__(self) -> None:
        self.repository = QuickTextRepository()
        self.adapter = QuickTextAdapter

    async def add_text(self, text: QuickText):
        try:
            await self.repository.create(self.adapter(text).to_schema())
            return True
        except:
            return False

    async def get_all_texts(self):
        texts_parsers = []
        texts = await self.repository.read()
        for text in texts:
            texts_parsers.append(self.adapter(text[0]).to_model())
        return texts_parsers

    async def update_text(self, quick_text: QuickText):
        try:
            await self.repository.update(self.adapter(quick_text).to_schema())
            return True
        except:
            return False

    async def delete_text(self, id: int):
        try:
            await self.repository.delete(id)
            return True
        except:
            return False
