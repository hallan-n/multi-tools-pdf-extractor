from app.adapters.implementations.template_adapter import TemplateAdapter
from app.domain.models.template import Template
from app.infrastructure.repositories.implementations.template_repository import \
    TemplateRepository


class TemplateUseCase:
    def __init__(self) -> None:
        self.repository = TemplateRepository()
        self.adapter = TemplateAdapter

    async def list_templates(self):
        template_parsers = []
        templates = await self.repository.read()
        for template in templates:
            template_parsers.append(self.adapter(template[0]).to_model())
        return template_parsers

    async def add_template(self, template: Template):
        try:
            await self.repository.create(self.adapter(template).to_schema())
            return True
        except:
            return False

    async def update_template(self, template: Template):
        try:
            await self.repository.update(self.adapter(template).to_schema())
            return True
        except:
            return False

    async def delete_template(self, id: int):
        try:
            await self.repository.delete(id)
            return True
        except:
            return False
