from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class QuickText(Base):
    __tablename__ = "quick_text"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)

    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="quick_texts")
