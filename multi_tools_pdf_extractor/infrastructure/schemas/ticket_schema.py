from sqlalchemy import Column, Integer, String, DateTime, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Ticket(Base):
    id = Column(Integer)
    open_date = Column(DateTime)
    resolution_date = Column(DateTime)
    owner = Column(String)
    status = Column(String)
    comments = Column(String)
    templates = Column(ARRAY(String))
