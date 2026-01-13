import os
from fastapi import FastAPI

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "dev")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": APP_ENV
    }
