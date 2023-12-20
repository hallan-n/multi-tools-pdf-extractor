from pydantic import BaseModel, validator


class Ticket(BaseModel):
    id: int
    author: int
    description: str

    @validator("description")
    def validate_description(cls, value):
        if not len(value):
            raise ValueError("")
        return value

    @validator("autor")
    def validate_author(cls, value):
        if not value:
            raise ValueError("")
        return value
