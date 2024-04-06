from fastapi import APIRouter

from app.domain.models.template import Template
from app.domain.use_cases.template_use_case import TemplateUseCase

route = APIRouter(tags=["Template"])


use_case = TemplateUseCase()


@route.get("/template")
async def list_templates():
    resp = await use_case.list_templates()
    return resp


@route.post("/template")
async def add_template(template: Template):
    resp = await use_case.add_template(template)
    return {"sucess": resp}


@route.put("/template")
async def update_template(template: Template):
    resp = await use_case.update_template(template)
    return {"sucess": resp}


@route.delete("/template")
async def delete_template(id: int):
    resp = await use_case.delete_template(id)
    return {"sucess": resp}
