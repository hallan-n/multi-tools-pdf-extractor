from sqlalchemy import Column, String
from .base import Base


class PDF(Base):
    title = Column(String)
    author = Column(String)
    content = Column(String)
    base64 = Column(String)
