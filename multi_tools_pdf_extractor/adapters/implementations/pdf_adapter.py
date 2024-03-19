from multi_tools_pdf_extractor.adapters.interfaces.data_parser import DataParser
from multi_tools_pdf_extractor.domain.models.pdf import PDF as Model
from multi_tools_pdf_extractor.infrastructure.schemas.pdf_schema import PDF as Schema


class PDFAdapter(DataParser):
    def __init__(self, model: Model, schema: Schema) -> None:
        self.model = model
        self.schema = schema

    def to_schema(self):
        fields = {}
        for prop in self.model:
            print(prop)

    def to_model(self):
        pass
