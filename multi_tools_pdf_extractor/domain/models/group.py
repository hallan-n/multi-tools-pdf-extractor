from pydantic import BaseModel, Field


class Group(BaseModel):
    group: str = Field(min_length=3, max_length=200)
