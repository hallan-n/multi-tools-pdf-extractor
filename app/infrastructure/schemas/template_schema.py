from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Template(Base):
    __tablename__ = "template"

    id = Column(Integer, primary_key=True, autoincrement=True)
    template = Column(String(200))

    ticket_id = Column(Integer, ForeignKey("ticket.id"))
    ticket = relationship("Ticket", back_populates="templates")
