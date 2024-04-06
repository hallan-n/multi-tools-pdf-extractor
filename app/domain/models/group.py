from pydantic import BaseModel


class Group(BaseModel):
    id: int = None
    group: str = None
    ticket_id: int = 0
    quick_text_id: int = 0
