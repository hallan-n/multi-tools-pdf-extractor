from sqlalchemy import Column, Integer, String, DateTime
from app.entities.schemas.base import Base
from datetime import datetime


class TicketSQL(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_ticket = Column(Integer, nullable=False, unique=True)
    link = Column(String(255), nullable=False, unique=True)
    group = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    create_at = Column(DateTime, default=datetime.now())
