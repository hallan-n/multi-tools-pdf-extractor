from pydantic import BaseModel
from .group import Group


class QuickText(BaseModel):
    text: str
    group: Group
