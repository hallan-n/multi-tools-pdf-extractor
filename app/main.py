from app.infrastructure.repositories.implementations.pdf_repository import PDFRepository
from app.infrastructure.schemas.pdf_schema import PDF
from app.infrastructure.schemas.ticket_schema import Ticket
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# import asyncio


@app.get("/")
async def inserir():
    ticket = Ticket()
    pdf = PDF(
        id=1,
        title="teste",
        author="teste",
        content="teste",
        base64="teste",
        ticket_id=1,
    )
    repo = PDFRepository()
    await repo.create(pdf)
    return "asd"
