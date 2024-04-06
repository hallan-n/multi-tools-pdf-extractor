from datetime import datetime

from fastapi import APIRouter

route = APIRouter()


@route.post("/quicktext")
async def add_text():
    from datetime import datetime

    from app.adapters.implementations.ticket_adapter import TicketAdapter
    from app.domain.models.ticket import Ticket as Model
    from app.infrastructure.schemas.brokerage_schema import Brokerage
    from app.infrastructure.schemas.group_schema import Group
    from app.infrastructure.schemas.quick_text_schema import QuickText
    from app.infrastructure.schemas.template_schema import Template
    from app.infrastructure.schemas.ticket_schema import Ticket as Schema

    now = datetime.now()
    schema = Schema(
        id=1,
        open_date=now,
        resolution_date=now,
        status="asd",
        comments="asd",
        is_sla=True,
    )
    # model = Model(id=1,open_date=now,resolution_date=now,status='asd',comments='asd',is_sla=True)
    adapt = TicketAdapter(schema)
    # adapt.to_schema()
    # print(schema)
    print(adapt.to_model())


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
