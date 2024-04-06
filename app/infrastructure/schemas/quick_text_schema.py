from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class QuickText(Base):
    __tablename__ = "quick_text"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(200))

    groups = relationship("Group", back_populates="quick_text")
