from pydantic import BaseModel


class Group(BaseModel):
    id: int = None
    group: str = None
