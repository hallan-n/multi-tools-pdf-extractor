from pydantic import BaseModel


class Template(BaseModel):
    id: int = None
    template: str = None
    ticket_id: int = None
