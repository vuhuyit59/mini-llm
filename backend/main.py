from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
from backend.core.logging_config import load_logging_config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_logging_config()

@app.get("/health-check")
async def health_check():
    return {"message": "Ok"}


app.include_router(
    router
)
