from app.infrastructure.repositories.implementations.group_repository import (
    GroupRepository,
)
from app.infrastructure.schemas.group_schema import Group
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# import asyncio


@app.get("/")
async def inserir():
    group = Group(id=2, group="Grupo update")
    repo = GroupRepository()
    rep = await repo.read()
    print(rep)

    return "asd"
