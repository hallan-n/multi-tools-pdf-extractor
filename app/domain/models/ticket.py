from pydantic import BaseModel
from datetime import date
from app.domain.models.group import Group
from app.domain.models.template import Template
from app.domain.models.pdf import PDF


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
