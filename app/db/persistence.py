from app.db.database import Database


class Persistence(Database):
    def __init__(self) -> None:
        ...

    def _create_table(self):
        self.create_tables()
