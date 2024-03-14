from sqlalchemy import Column, String
from .base import Base


class Group(Base):
    group = Column(String(200), min(3))


