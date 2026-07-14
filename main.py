"""Health service. """
import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app = FastAPI()
DEBUG = os.getenv("DEBUG", "false")


class HealthService:
    """Provides health status."""

    def status(self) -> dict:
        return {"status": "ok"}


@app.get("/health")
def health():
    """Health check endpoint."""
    service = HealthService()
    return service.status()
