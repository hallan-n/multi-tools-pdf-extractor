import trio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from ...schemas.base import Base


class Database:
    def __init__(self, database_url: str):
        self.engine = create_async_engine(database_url, echo=True, pool_size=10, max_overflow=20)
        self.async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)
        self.base = Base()
        trio.run(self.create_tables)

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
    async def __enter__(self):        
        return await self.async_session()

    async def __exit__(self, exc_type, exc_value, traceback):
        await self.async_session.close_all()















async def main():
    db = Database('DATABASE_URL')
    await db.create_tables()

if __name__ == "__main__":
    trio.run(main())



# def __enter__(self):
#     self.session = self.Session()
#     return self.session

# def __exit__(self, exc_type, exc_value, traceback):
#     if exc_type is not None:
#         self.session.rollback()
#     else:
#         self.session.commit()
#     self.session.close()

