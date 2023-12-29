from app.db.database import Database
from app.entities.ticket_sql import TicketSQL
from app.entities.ticket_model import Ticket


class TicketUseCases:
    def __init__(self) -> None:
        self.session = Database().get_session()

    def create_ticket(self, ticket: Ticket, rollback: bool = False):
        try:
            ticket_sql = TicketSQL(**ticket)
            self.session.add(ticket_sql)
            self.session.commit()
            if rollback:
                self.session.rollback()
            return True
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
