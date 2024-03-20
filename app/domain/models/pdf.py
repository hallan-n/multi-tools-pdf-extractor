from pydantic import BaseModel


class PDF(BaseModel):
    id: int = None
    title: str = None
    author: str = None
    content: str = None
    base64: str = None
