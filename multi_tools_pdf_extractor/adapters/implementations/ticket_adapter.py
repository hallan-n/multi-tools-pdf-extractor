from multi_tools_pdf_extractor.adapters.interfaces.data_parser import DataParser
from multi_tools_pdf_extractor.domain.models.ticket import Ticket as Model
from multi_tools_pdf_extractor.infrastructure.schemas.ticket_schema import (
    Ticket as Schema,
)


class TicketAdapter(DataParser):
    def __init__(self, model: Model, schema: Schema) -> None:
        self.model = model
        self.schema = schema

    def to_schema(self):
        pass

    def to_model(self):
        pass
