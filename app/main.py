from fastapi import FastAPI


class App(FastAPI):
    def __init__(self, *argS, **kwargs) -> None:
        super().__init__(*argS, **kwargs)


app = App()


@app.get("/")
async def entry():
    return "Rodando"
