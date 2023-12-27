from fastapi import FastAPI
import os
from db.database import Database


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    # def include_routers(self):
    #     self.include_router()


app = App()


@app.get("/")
async def entry():
    DB_URL = f'mysql+mysqlconnector://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}/{os.environ.get("DB_DATABASE")}'
    db = Database(DB_URL)
    return db
