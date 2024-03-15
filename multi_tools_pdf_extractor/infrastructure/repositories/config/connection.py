import os
import trio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from ...schemas.base import Base

URL = os.environ.get("CONNECTION_STRING")


class Connection:
    def __init__(self):
        trio.run(self.create_tables)
        self.engine = create_async_engine(URL, echo=True, pool_size=10, max_overflow=20)
        self.async_session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )
        self.base = Base()

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def __aenter__(self):
        return self.async_session()

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.async_session().close()
