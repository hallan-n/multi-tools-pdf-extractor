from fastapi import FastAPI
from app.use_cases.ticket_use_case import TicketUseCases

app = FastAPI()


@app.get("/")
async def entry():
    ticker_use_cases = TicketUseCases()
    return "Rodando"
