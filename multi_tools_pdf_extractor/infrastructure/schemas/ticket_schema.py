from sqlalchemy import Column, Integer, String, DateTime, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    open_date = Column(DateTime)
    resolution_date = Column(DateTime)
    owner = Column(String(200))
    status = Column(String(200))
    comments = Column(String(200))

    templates = relationship("Template", back_populates="ticket_id")
    pdfs = relationship("PDF", back_populates="ticket_id")

    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="tickets")
