from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    settings = get_settings()
    print(f"Starting app in {settings.app_env} mode")
    # TODO: Connect Redis, DB, etc.

    yield  # App runs here (between startup and shutdown)

    # Shutdown logic
    print("Shutting down cleanly...")
    # TODO: Cleanup Redis, containers, etc.


app = FastAPI(title="CCE", lifespan=lifespan)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check
@app.get("/ping", tags=["health"])
async def ping():
    return {"message": "pong"}
