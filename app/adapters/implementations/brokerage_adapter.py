from app.adapters.interfaces.data_parser import DataParser
from app.domain.models.brokerage import Brokerage as Model
from app.infrastructure.schemas.brokerage_schema import Brokerage as Schema
from app.infrastructure.schemas.group_schema import Group
from app.infrastructure.schemas.quick_text_schema import QuickText
from app.infrastructure.schemas.template_schema import Template
from app.infrastructure.schemas.ticket_schema import Ticket


class BrokerageAdapter(DataParser):
    def __init__(self, brokerage: Model | Schema) -> None:
        self.brokerage = brokerage

    def to_schema(self):
        if isinstance(self.brokerage, Schema):
            return self.brokerage
        try:
            data = self.brokerage.model_dump()
            return Schema(**data)
        except Exception as e:
            raise e

    def to_model(self):
        try:
            data = vars(self.brokerage)
            del data["_sa_instance_state"]
            return Model(**data)
        except Exception as e:
            raise e
