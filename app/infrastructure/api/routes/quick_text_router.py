from fastapi import APIRouter

from app.domain.models.quick_text import QuickText
from app.domain.use_cases.quick_text_use_case import QuickTextUseCase

route = APIRouter(tags=["Quick texts"])

use_case = QuickTextUseCase()


@route.post("/quicktext")
async def add_text(text: QuickText):
    resp = await use_case.add_text(text)
    return {"sucess": resp}


@route.get("/quicktext")
async def get_all_texts():
    resp = await use_case.get_all_texts()
    return resp


@route.put("/quicktext")
async def update_text(quick_text: QuickText):
    resp = await use_case.update_text(quick_text)
    return {"sucess": resp}


@route.delete("/quicktext")
async def delete_text(id: int):
    resp = await use_case.delete_text(id)
    return {"sucess": resp}
