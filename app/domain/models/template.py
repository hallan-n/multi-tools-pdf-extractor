from pydantic import BaseModel
from app.domain.models.group import Group


class Template(BaseModel):
    id: int = None
    template: str = None
