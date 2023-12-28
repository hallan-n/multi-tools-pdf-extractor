from fastapi import FastAPI
from app.db.database import Database
import os


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


app = App()


@app.get("/")
async def entry():
    DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'
    db = Database(DB_URL)
    db.is_connect()
    return "Não conecto"
