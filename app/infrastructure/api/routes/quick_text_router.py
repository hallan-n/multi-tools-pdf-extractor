from fastapi import APIRouter
from datetime import datetime

now = datetime.now()

route = APIRouter()


@route.post("/quicktext")
async def add_text():
    from app.infrastructure.schemas.quick_text_schema import QuickText
    from app.infrastructure.schemas.group_schema import Group
    from app.infrastructure.schemas.ticket_schema import Ticket
    from app.infrastructure.schemas.brokerage_schema import Brokerage
    from app.infrastructure.schemas.template_schema import Template

    template = Template(id=1, template="asd")
    brokerage = Brokerage(id=1, brokerage="asd")
    ticket = Ticket(
        open_date=now, resolution_date=now, status="asd", comments="asd", is_sla=True
    )
    group = Group(group="asd", ticket_id=1)
    text = QuickText(id=1, text="asdasd")


# @route.get("/quicktext")
# async def get_all_texts():
#     ...


# @route.post("/quicktext")
# async def update_text(quick_text: QuickText):
#     ...


# @route.delete("/quicktext")
# async def delete_text(quick_text: QuickText):
#     ...


# @route.post("/quicktext")
# async def add_group(quick_text: QuickText, group: Group):
#     ...
