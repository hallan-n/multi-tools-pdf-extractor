from app.adapters.interfaces.data_parser import DataParser
from app.domain.models.quick_text import QuickText as Model
from app.infrastructure.schemas.brokerage_schema import Brokerage
from app.infrastructure.schemas.group_schema import Group
from app.infrastructure.schemas.quick_text_schema import QuickText as Schema
from app.infrastructure.schemas.template_schema import Template
from app.infrastructure.schemas.ticket_schema import Ticket


class QuickTextAdapter(DataParser):
    def __init__(self, text: Model | Schema) -> None:
        self.text = text

    def to_schema(self):
        if isinstance(self.text, Schema):
            return self.text
        try:
            data = self.text.model_dump()
            return Schema(**data)
        except Exception as e:
            raise e

    def to_model(self):
        try:
            data = vars(self.text)
            del data["_sa_instance_state"]
            return Model(**data)
        except Exception as e:
            raise e
