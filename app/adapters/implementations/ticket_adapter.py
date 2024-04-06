from app.adapters.interfaces.data_parser import DataParser
from app.domain.models.ticket import Ticket as Model
from app.infrastructure.schemas.brokerage_schema import Brokerage
from app.infrastructure.schemas.group_schema import Group
from app.infrastructure.schemas.quick_text_schema import QuickText
from app.infrastructure.schemas.template_schema import Template
from app.infrastructure.schemas.ticket_schema import Ticket as Schema


class TicketAdapter(DataParser):
    def __init__(self, ticket: Model | Schema) -> None:
        self.ticket = ticket

    def to_schema(self):
        if isinstance(self.ticket, Schema):
            return self.ticket
        try:
            data = self.ticket.model_dump()
            return Schema(**data)
        except Exception as e:
            raise e

    def to_model(self):
        if isinstance(self.ticket, Model):
            return self.ticket
        try:
            data = vars(self.ticket)
            del data["_sa_instance_state"]
            return Model(**data)
        except Exception as e:
            raise e
