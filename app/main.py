from fastapi import FastAPI


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    # def include_routers(self):
    #     self.include_router()


app = App()


@app.get("/")
async def entry():
    return "Rodando"
