from app.entities.base import Base
from app.entities.ticket_sql import TicketSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.Session()
        yield session
        session.close()

    def is_connect(self):
        return not self.engine.connect()._is_disconnect

    def create_tables(self, rollback: bool = False):
        try:
            Base.metadata.create_all(bind=self.engine)
            if rollback:
                Base.metadata.drop_all(bind=self.engine)
            return True
        except Exception as e:
            print(f"Error creating tables: {e}")
            return False
