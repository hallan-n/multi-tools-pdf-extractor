from datetime import datetime

from pydantic import BaseModel


class Ticket(BaseModel):
    id: int = None
    open_date: datetime = None
    resolution_date: datetime = None
    status: str = None
    comments: str = None
    is_sla: bool = None
