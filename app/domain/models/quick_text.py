from pydantic import BaseModel
from domain.models.group import Group


class QuickText(BaseModel):
    id: int = None
    text: str = None
    group: Group = None
