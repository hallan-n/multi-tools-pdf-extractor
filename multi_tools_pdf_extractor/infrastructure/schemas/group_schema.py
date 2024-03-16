from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .base import Base


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, autoincrement=True)
    group = Column(String(200))

    tickets = relationship("Ticket", back_populates="group_id")
    quick_texts = relationship("QuickText", back_populates="group_id")
