from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()


# Configure o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

from app.infrastructure.api.routes.pdf_router import router as pdf
from app.infrastructure.api.routes.quick_text_router import route as text

app.include_router(pdf)
app.include_router(text)
