from sqlalchemy import Column, String
from .base import Base
from .group_schema import Group



class QuickText(Base):
    text = Column(String)
    group = Column(String)
