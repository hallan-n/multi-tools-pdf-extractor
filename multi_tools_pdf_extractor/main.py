import asyncio
from infrastructure.repositories.config.connection import Connection
from dotenv import load_dotenv

load_dotenv()


async def teste():
    async with Connection() as conn:
        ...


loop = asyncio.get_event_loop()
loop.run_until_complete(teste())
