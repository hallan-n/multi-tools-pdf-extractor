from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    open_date = Column(DateTime)
    resolution_date = Column(DateTime)
    status = Column(String(200))
    title = Column(String(200))
    url = Column(String(200))
    comments = Column(String(200))
    is_sla = Column(Boolean, default=False)

    templates = relationship("Template", back_populates="ticket")
    groups = relationship("Group", back_populates="ticket")
    brokerage = relationship("Brokerage", uselist=False, back_populates="ticket")
