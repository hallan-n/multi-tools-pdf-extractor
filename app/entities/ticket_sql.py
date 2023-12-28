from sqlalchemy import Column, Integer, String
from entities.base import Base


class TicketSQL(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ticket = Column(Integer, nullable=False, unique=True)
    link = Column(String(255), nullable=False, unique=True)
    group = Column(String(255), nullable=True, unique=True)
    description = Column(String(255), nullable=True)
