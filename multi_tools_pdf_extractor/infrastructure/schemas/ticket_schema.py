from sqlalchemy import Column, Integer, String, DateTime, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer)
    open_date = Column(DateTime)
    resolution_date = Column(DateTime)
    owner = Column(String)
    status = Column(String)
    comments = Column(String)
    templates = Column(ARRAY(String))

    pdfs = relationship("PDF", back_populates="ticket_id")

    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="tickets")
