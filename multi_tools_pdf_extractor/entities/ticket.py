from pydantic import BaseModel
from datetime import date


class Ticket(BaseModel):
    id: int
    open_date: date
    resolution_date: date
    owner: str
    status: str
    comments: str
    templates: list[str] | str
