from app.entities.base import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.entities.ticket_sql import TicketSQL
import os


class Database:
    _DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'

    def __init__(self, db_url: str = _DB_URL) -> None:
        self.engine = create_engine(db_url, pool_size=5, max_overflow=10)
        self.metadata = MetaData()
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.create_tables()

    def get_session(self):
        return self.Session()

    def is_connect(self):
        return not self.engine.connect()._is_disconnect

    def create_tables(self):
        try:
            self.metadata.reflect(bind=self.engine)
            if not self.metadata.tables:
                Base.metadata.create_all(bind=self.engine)
                return True
        except Exception as e:
            raise e
