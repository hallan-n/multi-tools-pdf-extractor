from fastapi import FastAPI

# from app.db.database import Database
# from app.entities.ticket_sql import TicketSQL
# import os


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


app = App()


@app.get("/")
async def entry():
    asd = "asdf vb wfvwqef"
    return "Não conecto"
