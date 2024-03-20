from multi_tools_pdf_extractor.adapters.interfaces.data_parser import DataParser
from multi_tools_pdf_extractor.domain.models.pdf import PDF as Model
from multi_tools_pdf_extractor.infrastructure.schemas.pdf_schema import PDF as Schema


class PDFAdapter(DataParser):
    def __init__(self, pdf: Model | Schema) -> None:
        self.pdf = pdf

    def to_schema(self):
        try:
            data = dict(self.pdf)
            return Schema(**data)
        except Exception as e:
            raise e

    def to_model(self):
        pdf = {}

        ticket = vars(vars(self.pdf).get("ticket"))
        return ticket
