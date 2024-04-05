from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, autoincrement=True)
    group = Column(String(200))

    ticket_id = Column(Integer, ForeignKey("ticket.id"))
    ticket = relationship("Ticket", back_populates="groups")

    quick_text_id = Column(Integer, ForeignKey("quick_text.id"))
    quick_text = relationship("QuickText", back_populates="groups")
