import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.schemas.base import Base
from app.infrastructure.schemas.group_schema import Group
from app.infrastructure.schemas.quick_text_schema import QuickText
from app.infrastructure.schemas.template_schema import Template
from app.infrastructure.schemas.ticket_schema import Ticket


class Connection:
    def __init__(self):
        self.engine = create_async_engine(
            os.getenv("CONNECTION_STRING"), echo=True, pool_size=10, max_overflow=20
        )
        self.async_session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )
        self.base = Base()

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(self.base.metadata.create_all)

    async def __aenter__(self):
        await self.create_tables()
        return self.async_session()

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.async_session().close()
