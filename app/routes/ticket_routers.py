from fastapi import APIRouter


class TicketRouter(APIRouter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setup_router()

    def setup_router(self):
        @self.get("/tickets")
        def create_ticket():
            return {"mensagem": "Criado"}
