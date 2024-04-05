from pydantic import BaseModel
from app.domain.models.group import Group


class QuickText(BaseModel):
    id: int = None
    text: str = None
    group: list[Group] = None
