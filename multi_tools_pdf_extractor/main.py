from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def teste(pdf: PDF):
    return "ok"
