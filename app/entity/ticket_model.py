from pydantic import BaseModel, validator
import re


class Ticket(BaseModel):
    id: int = None
    id_ticket: int = None
    link: str = None
    description: str = None

    @validator("id_ticket")
    def validate_id(cls, value):
        if not isinstance(value, int):
            raise ValueError("O ID deve receber um valor numérico inteiro!")
        return True

    @validator("link")
    def validate_link(cls, value):
        url = re.compile("^(https):\/\/[^\s/$.?#].[^\s]*$")
        if not url.match(value) and not len(value) > 255:
            raise ValueError("URL no formato inválido!")
        return True

    @validator("description")
    def validate_id(cls, value):
        if len(value) > 255:
            raise ValueError("A descrição deve ter no máximo 255 caracteres")
        return True
