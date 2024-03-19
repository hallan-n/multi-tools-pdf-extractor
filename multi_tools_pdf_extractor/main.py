from fastapi import FastAPI
from multi_tools_pdf_extractor.infrastructure.api.routes.ticket_router import (
    router as ticket_router,
)

app = FastAPI()

app.include_router(ticket_router)
