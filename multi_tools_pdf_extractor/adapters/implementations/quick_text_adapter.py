from multi_tools_pdf_extractor.adapters.interfaces.data_parser import DataParser
from multi_tools_pdf_extractor.domain.models.quick_text import QuickText as Model
from multi_tools_pdf_extractor.infrastructure.schemas.quick_text_schema import (
    QuickText as Schema,
)


class QuickTextAdapter(DataParser):
    def __init__(self, model: Model, schema: Schema) -> None:
        self.model = model
        self.schema = schema

    def to_schema(self):
        pass

    def to_model(self):
        pass
