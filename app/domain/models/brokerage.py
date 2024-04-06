from pydantic import BaseModel


class Brokerage(BaseModel):
    id: int = None
    brokerage: str = None
    ticket_id: int = None
