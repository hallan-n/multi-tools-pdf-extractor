from fastapi import APIRouter

from app.domain.models.group import Group
from app.domain.use_cases.group_use_case import GroupUseCase

route = APIRouter(tags=["Group"])


use_case = GroupUseCase()


@route.get("/group")
async def list_groups():
    resp = await use_case.list_groups()
    return resp


@route.post("/group")
async def add_group(group: Group):
    resp = await use_case.add_group(group)
    return {"sucess": resp}


@route.put("/group")
async def update_group(group: Group):
    resp = await use_case.update_group(group)
    return {"sucess": resp}


@route.delete("/group")
async def update_group(id: int):
    resp = await use_case.delete_group(id)
    return {"sucess": resp}
