from fastapi import FastAPI
from app.routes.ticket_routers import TicketRouter


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.load_routers()

    def load_routers(self):
        self.include_router(TicketRouter())
