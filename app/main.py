from fastapi import FastAPI
from app.db.database import Database

app = FastAPI()


@app.get("/")
async def entry():
    return "Rodando"
