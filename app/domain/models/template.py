from pydantic import BaseModel
from domain.models.group import Group


class Template(BaseModel):
    id: int = None
    template: str = None
