from pydantic import BaseModel
from datetime import date
from multi_tools_pdf_extractor.domain.models.group import Group
from multi_tools_pdf_extractor.domain.models.template import Template
from multi_tools_pdf_extractor.domain.models.pdf import PDF


class Ticket(BaseModel):
    id: int = None
    open_date: date = None
    resolution_date: date = None
    owner: str = None
    status: str = None
    comments: str = None
    templates: list[Template] = None
    pdfs: list[PDF] = None
    group: Group = None
