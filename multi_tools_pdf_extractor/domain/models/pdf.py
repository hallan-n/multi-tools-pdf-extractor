from pydantic import BaseModel


class PDF(BaseModel):
    title: str
    author: str
    content: str
    base64: str
