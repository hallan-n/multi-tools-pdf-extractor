from sqlalchemy.orm import declarative_base
from .group_schema import Group
from .pdf_schema import PDF
from .quick_text_schema import QuickText
from .ticket_schema import Ticket

BaseModel = declarative_base()


class Base(BaseModel):
    __abstract__ = True
