from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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

    pdfs = relationship("PDF", back_populates="ticket")
    templates = relationship("Template", back_populates="ticket")

    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="tickets")
