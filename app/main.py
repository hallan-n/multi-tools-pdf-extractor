from fastapi import FastAPI
from app.db.database import Database
import os


app = FastAPI()


@app.get("/")
async def entry():
    try:
        DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'
        db = Database(DB_URL)
        db.is_connect()
        return "Rodando"
    except:
        return "Não conectou"
