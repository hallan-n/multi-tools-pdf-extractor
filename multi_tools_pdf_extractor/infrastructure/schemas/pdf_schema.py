from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class PDF(Base):
    __tablename__ = "pdf"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200))
    author = Column(String(200))
    content = Column(String(200))
    base64 = Column(String(200))

    ticket_id = Column(Integer, ForeignKey("ticket.id"))
    ticket = relationship("Ticket", back_populates="pdfs")
