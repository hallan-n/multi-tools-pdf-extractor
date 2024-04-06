from fastapi import APIRouter

from app.domain.models.ticket import Ticket
from app.domain.use_cases.ticket_use_case import TicketUseCase

route = APIRouter(tags=["Ticket"])


use_case = TicketUseCase()


@route.get("/ticket")
async def list_tickets():
    resp = await use_case.list_tickets()
    return {"sucess": resp}


@route.post("/ticket")
async def add_ticket(ticket: Ticket):
    resp = await use_case.add_ticket(ticket)
    return {"sucess": resp}


@route.put("/ticket")
async def update_ticket(ticket: Ticket):
    resp = await use_case.update_ticket(ticket)
    return {"sucess": resp}


@route.delete("/ticket")
async def update_ticket(id: int):
    resp = await use_case.delete_ticket(id)
    return {"sucess": resp}
