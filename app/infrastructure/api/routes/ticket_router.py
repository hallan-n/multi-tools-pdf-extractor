from fastapi import APIRouter
from app.domain.models.ticket import Ticket
from app.domain.models.group import Group

route = APIRouter()


@route.get("/ticket")
async def list_tickets():
    ...


@route.post("/ticket")
async def add_ticket(ticket: Ticket):
    ...


@route.post("/ticket")
async def add_group(ticket: Ticket, group: Group):
    ...
