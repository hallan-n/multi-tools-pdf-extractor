from app.entities.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        session = self.Session()
        yield session
        session.close()

    def get_connection(self):
        self.engine.connect()

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)
