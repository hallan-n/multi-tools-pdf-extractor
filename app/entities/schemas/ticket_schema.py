from pydantic import BaseModel, validator
from datetime import date
import re


class Ticket(BaseModel):
    id: int = None
    id_ticket: int = None
    link: str = None
    group: str = None
    description: str = None
    create_at: date = None

    @validator("id_ticket")
    def validate_id(cls, value):
        if not isinstance(value, int):
            raise ValueError("O ID deve receber um valor numérico inteiro!")
        return value

    @validator("link")
    def validate_link(cls, value):
        url = re.compile("^(http(s)?):\/\/[^\s/$.?#].[^\s]*$")
        if not url.match(value) and not len(value) > 255:
            raise ValueError("URL no formato inválido!")
        return value

    @validator("group")
    def validate_group(cls, value):
        if len(value) > 255:
            raise ValueError("A descrição deve ter no máximo 255 caracteres")
        return value

    @validator("description")
    def validate_description(cls, value):
        if len(value) > 255:
            raise ValueError("A descrição deve ter no máximo 255 caracteres")
        return value
