from pydantic import BaseModel
from multi_tools_pdf_extractor.domain.models.group import Group


class QuickText(BaseModel):
    id: int = None
    text: str = None
    group: Group = None
