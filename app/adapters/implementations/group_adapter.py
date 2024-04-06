from app.adapters.interfaces.data_parser import DataParser
from app.domain.models.group import Group as Model
from app.infrastructure.schemas.brokerage_schema import Brokerage
from app.infrastructure.schemas.group_schema import Group as Schema
from app.infrastructure.schemas.quick_text_schema import QuickText
from app.infrastructure.schemas.template_schema import Template
from app.infrastructure.schemas.ticket_schema import Ticket


class GroupAdapter(DataParser):
    def __init__(self, group: Model | Schema) -> None:
        self.group = group

    def to_schema(self):
        if isinstance(self.template, Schema):
            return self.template
        try:
            data = self.group.model_dump()
            return Schema(**data)
        except Exception as e:
            raise e

    def to_model(self):
        try:
            data = vars(self.group)
            del data["_sa_instance_state"]
            return Model(**data)
        except Exception as e:
            raise e
