from pydantic import BaseModel
from datetime import date
from multi_tools_pdf_extractor.domain.models.template import Template
from multi_tools_pdf_extractor.domain.models.group import Group


class Ticket(BaseModel):
    id: int = None
    open_date: date = None
    resolution_date: date = None
    owner: str = None
    status: str = None
    comments: str = None
    templates: list[Template] | Template = None
    group: Group
