from app.db.database import Database


class TicketUseCases:
    def ____init__(self) -> None:
        self.session = Database().get_session()
