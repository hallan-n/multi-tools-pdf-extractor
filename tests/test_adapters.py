from datetime import datetime

from app.adapters.implementations.brokerage_adapter import BrokerageAdapter
from app.adapters.implementations.group_adapter import GroupAdapter
from app.adapters.implementations.quick_text_adapter import QuickTextAdapter
from app.adapters.implementations.template_adapter import TemplateAdapter
from app.adapters.implementations.ticket_adapter import TicketAdapter
from app.domain.models.brokerage import Brokerage as BrokerageModel
from app.domain.models.group import Group as GroupModel
from app.domain.models.quick_text import QuickText as QuickTextModel
from app.domain.models.template import Template as TemplateModel
from app.domain.models.ticket import Ticket as TicketModel
from app.infrastructure.schemas.brokerage_schema import \
    Brokerage as BrokerageSchema
from app.infrastructure.schemas.group_schema import Group as GroupSchema
from app.infrastructure.schemas.quick_text_schema import \
    QuickText as QuickTextSchema
from app.infrastructure.schemas.template_schema import \
    Template as TemplateSchema
from app.infrastructure.schemas.ticket_schema import Ticket as TicketSchema

now = datetime.now()


def test_brokerage_adapter():
    brokerage_schema = BrokerageSchema(id=1, brokerage="agrega", ticket_id=1)
    brokerage_model = BrokerageModel(id=1, brokerage="agrega", ticket_id=1)
    assert isinstance(BrokerageAdapter(brokerage_schema).to_model(), BrokerageModel)
    assert isinstance(BrokerageAdapter(brokerage_model).to_schema(), BrokerageSchema)


def test_group_adapter():
    group_schema = GroupSchema(id=1, group="teste", ticket_id=1, quick_text_id=1)
    group_model = GroupModel(id=1, group="teste", ticket_id=1, quick_text_id=1)
    assert isinstance(GroupAdapter(group_schema).to_model(), GroupModel)
    assert isinstance(GroupAdapter(group_model).to_schema(), GroupSchema)


def test_quick_text_adapter():
    quick_text_schema = QuickTextSchema(id=1, text="teste")
    quick_text_model = QuickTextModel(id=1, text="teste")
    assert isinstance(QuickTextAdapter(quick_text_schema).to_model(), QuickTextModel)
    assert isinstance(QuickTextAdapter(quick_text_model).to_schema(), QuickTextSchema)


def test_template_adapter():
    template_schema = TemplateSchema(id=1, template="asd", ticket_id=1)
    template_model = TemplateModel(id=1, template="asd", ticket_id=1)
    assert isinstance(TemplateAdapter(template_schema).to_model(), TemplateModel)
    assert isinstance(TemplateAdapter(template_model).to_schema(), TemplateSchema)


def test_ticket_adapter():
    ticket_schema = TicketSchema(
        id=1,
        open_date=now,
        resolution_date=now,
        status="asd",
        comments="asd",
        is_sla=True,
    )
    ticket_model = TicketModel(
        id=1,
        open_date=now,
        resolution_date=now,
        status="asd",
        comments="asd",
        is_sla=True,
    )
    assert isinstance(TicketAdapter(ticket_schema).to_model(), TicketModel)
    assert isinstance(TicketAdapter(ticket_model).to_schema(), TicketSchema)
