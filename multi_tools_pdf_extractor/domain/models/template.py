from pydantic import BaseModel


class Template(BaseModel):
    template: str = None
