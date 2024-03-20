from app.adapters.interfaces.data_parser import DataParser
from app.domain.models.quick_text import QuickText as Model
from app.infrastructure.schemas.quick_text_schema import (
    QuickText as Schema,
)


class QuickTextAdapter(DataParser):
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
            print(Model(**data))
            # return Model(**data)
        except Exception as e:
            raise e
