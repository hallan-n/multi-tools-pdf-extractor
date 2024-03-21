from pydantic import BaseModel
from datetime import date
from app.domain.models.group import Group
from app.domain.models.template import Template


class Ticket(BaseModel):
    id: int = None
    open_date: date = None
    resolution_date: date = None
    owner: str = None
    status: str = None
    comments: str = None
    templates: list[Template] = None
    group: Group = None
