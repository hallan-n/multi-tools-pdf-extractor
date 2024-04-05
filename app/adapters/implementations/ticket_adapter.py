from adapters.interfaces.data_parser import DataParser
from domain.models.ticket import Ticket as Model
from infrastructure.schemas.ticket_schema import (
    Ticket as Schema,
)


class TicketAdapter(DataParser):
    def __init__(self, ticket: Model | Schema) -> None:
        self.ticket = ticket

    def to_schema(self):
        try:
            data = self.ticket.model_dump()
            print(data)
        except Exception as e:
            raise e

    def to_model(self):
        try:
            data = vars(self.pdf)
            return Model(**data)
        except Exception as e:
            raise e
