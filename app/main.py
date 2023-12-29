from fastapi import FastAPI
from app.db.database import Database
import os


app = FastAPI()


@app.get("/")
async def entry():
    try:
        db = Database()
        db.is_connect()
        return "Rodando"
    except:
        return "Não conectou"
