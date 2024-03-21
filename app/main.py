from fastapi import FastAPI
from app.domain.models.ticket import Ticket
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.post("/")
async def inserir(quick_text: Ticket):
    return "asd"
