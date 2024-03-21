from adapters.interfaces.data_parser import DataParser
from domain.models.ticket import Ticket as Model
from infrastructure.schemas.ticket_schema import (
    Ticket as Schema,
)


class TicketAdapter(DataParser):
    def __init__(self, pdf: Model | Schema) -> None:
        self.pdf = pdf

    def to_schema(self):
        try:
            data = dict(self.pdf)
            return Schema(**data)
        except Exception as e:
            raise e

    def to_model(self):
        try:
            data = vars(self.pdf)
            return Model(**data)
        except Exception as e:
            raise e
