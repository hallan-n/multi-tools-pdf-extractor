from app.adapters.interfaces.data_parser import DataParser
from app.domain.models.template import Template as Model
from app.infrastructure.schemas.brokerage_schema import Brokerage
from app.infrastructure.schemas.group_schema import Group
from app.infrastructure.schemas.quick_text_schema import QuickText
from app.infrastructure.schemas.template_schema import Template as Schema
from app.infrastructure.schemas.ticket_schema import Ticket


class TemplateAdapter(DataParser):
    def __init__(self, template: Model | Schema) -> None:
        self.template = template

    def to_schema(self):
        if isinstance(self.template, Schema):
            return self.template
        try:
            data = self.template.model_dump()
            return Schema(**data)
        except Exception as e:
            raise e

    def to_model(self):
        if isinstance(self.template, Model):
            return self.template
        try:
            data = vars(self.template)
            del data["_sa_instance_state"]
            return Model(**data)
        except Exception as e:
            raise e
