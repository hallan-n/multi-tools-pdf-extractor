import pytest
from multi_tools_pdf_extractor.infrastructure.repositories.config.connection import (
    Connection,
)


@pytest.fixture
async def connection():
    async with Connection() as conn:
        yield conn
@pytest.mark.asyncio
async def test_connection(connection):
    assert connection is not None
@pytest.mark.asyncio
async def test_create_tables(connection):
    assert await connection.execute("SELECT 1") is not None
@pytest.mark.asyncio
async def test_session_closing():
    async with Connection() as conn:
        pass
    assert conn.closed