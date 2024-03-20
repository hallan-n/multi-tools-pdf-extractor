from app.adapters.interfaces.data_parser import DataParser
from app.domain.models.pdf import PDF as Model
from app.infrastructure.schemas.pdf_schema import PDF as Schema


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
        try:
            data = vars(self.pdf)
            return Model(**data)
        except Exception as e:
            raise e
