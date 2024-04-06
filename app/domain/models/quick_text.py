from pydantic import BaseModel


class QuickText(BaseModel):
    id: int = None
    text: str = None
