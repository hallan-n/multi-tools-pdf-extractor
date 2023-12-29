from app.entities.base import Base
from app.entities.ticket_sql import TicketSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class Database:
    _DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'

    def __init__(self, db_url: str = _DB_URL) -> None:
        self.engine = create_engine(db_url, pool_size=5, max_overflow=10)
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.Session()

    def is_connect(self):
        return not self.engine.connect()._is_disconnect

    def create_tables(self):
        try:
            Base.metadata.create_all(bind=self.engine)
            return True
        except Exception as e:
            raise e
