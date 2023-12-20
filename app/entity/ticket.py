from pydantic import BaseModel, validator

class Ticket(BaseModel):
    id: int
    description: str

    @validator("description")
    def validate_description(cls, value):
        if len(value):
            raise ValueError("")
        return value