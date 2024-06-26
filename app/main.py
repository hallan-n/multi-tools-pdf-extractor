from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

from app.infrastructure.api.routes.group_router import route as group
from app.infrastructure.api.routes.pdf_router import router as pdf
from app.infrastructure.api.routes.quick_text_router import route as text
from app.infrastructure.api.routes.template_router import route as template
from app.infrastructure.api.routes.ticket_router import route as ticket

app.include_router(pdf)
app.include_router(text)
app.include_router(ticket)
app.include_router(group)
app.include_router(template)
