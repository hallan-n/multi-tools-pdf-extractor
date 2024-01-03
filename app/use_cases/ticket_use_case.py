from app.db.database import Database
from app.entities.models.ticket_model import TicketSQL
from app.entities.schemas.ticket_schema import Ticket


class TicketUseCases:
    def __init__(self) -> None:
        self.session = Database().get_session()

    def create_ticket(self, ticket: Ticket, rollback: bool = False):
        try:
            ticket_model = TicketSQL(**dict(ticket))
            self.session.add(ticket_model)
            # Com finalidade de testes
            if rollback:
                self.session.rollback()
                return True
            self.session.commit()
            return ticket
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def select_tickets(self, page: int, page_size: int, tests: bool = False):
        try:
            tickets = (
                self.session.query(TicketSQL)
                .limit(page_size)
                .offset((page - 1) * page_size)
                .all()
            )
            # Com finalidade de testes
            if tests:
                return True
            return tickets
        except Exception as e:
            raise e
        finally:
            self.session.close()
