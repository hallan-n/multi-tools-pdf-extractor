from pydantic import BaseModel
from multi_tools_pdf_extractor.domain.models.group import Group


class Template(BaseModel):
    id: int = None
    template: str = None
