from fastapi import APIRouter
from app.domain.models.quick_text import QuickText
from domain.models.group import Group

route = APIRouter()


@route.post("/quicktext")
async def add_text(quick_text: QuickText):
    ...


@route.get("/quicktext")
async def get_all_texts():
    ...


@route.post("/quicktext")
async def update_text(quick_text: QuickText):
    ...


@route.delete("/quicktext")
async def delete_text(quick_text: QuickText):
    ...


@route.post("/quicktext")
async def add_group(quick_text: QuickText, group: Group):
    ...
