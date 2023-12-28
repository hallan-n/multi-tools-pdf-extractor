from fastapi import FastAPI
from db.database import Database
from entities.ticket_sql import TicketSQL
import os


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


app = App()


@app.get("/")
async def entry():
    try:
        DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'
        db = Database(DB_URL)
        return "Conectou"
    except:
        return "Não conectou"
