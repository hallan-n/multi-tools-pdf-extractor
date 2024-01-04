from app.entities.schemas.base import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.entities.models.ticket_model import TicketSQL
from os import environ


class Database:
    def __init__(
        self,
        db_url: str = f'mysql+mysqlconnector://{environ.get("DB_USER")}:{environ.get("DB_PASSWORD")}@{environ.get("DB_HOST")}/{environ.get("DB_DATABASE")}',
    ) -> None:
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
