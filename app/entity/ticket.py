from pydantic import BaseModel, validator


class Ticket(BaseModel):
    id: int = None
    author: int = None
    description: str = None

    @validator("id")
    def validate_id(cls, value):
        if not isinstance(value, int):
            raise ValueError("O ID deve receber um valor numérico inteiro!")
        return True

    @validator("author")
    def validate_id(cls, value):
        if not isinstance(value, int):
            raise ValueError("O Autor deve receber um valor numérico inteiro!")
        return True

    @validator("description")
    def validate_id(cls, value):
        if len(value) > 255:
            raise ValueError("A descrição deve ter no máximo 255 caracteres")
        return True
