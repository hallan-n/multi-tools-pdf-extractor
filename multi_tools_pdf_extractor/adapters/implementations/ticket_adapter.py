from multi_tools_pdf_extractor.adapters.interfaces.data_parser import DataParser
from multi_tools_pdf_extractor.domain.models.ticket import Ticket as Model
from multi_tools_pdf_extractor.infrastructure.schemas.ticket_schema import (
    Ticket as Schema,
)


class TicketAdapter(DataParser):
    def __init__(self, ticket: Model | Schema) -> None:
        self.ticket = ticket

    def to_schema(self):
        try:
            data = dict(self.ticket)
            return Schema(**data)
        except Exception as e:
            raise e("Erro ao fazer cast de Model para Schema")

    def to_model(self):
        pass
