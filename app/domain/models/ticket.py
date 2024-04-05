from pydantic import BaseModel
from datetime import date
from app.domain.models.group import Group
from app.domain.models.template import Template
from app.domain.models.brokerage import Brokerage


class Ticket(BaseModel):
    id: int = None
    open_date: date = None
    resolution_date: date = None
    status: str = None
    comments: str = None
    is_sla: bool = None
    brokerage: Brokerage = None
    templates: list[Template] = None
    group: list[Group] = None
