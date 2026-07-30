from contextlib import asynccontextmanager

from fastapi import FastAPI

APP_NAME = "Vacanze Sicure nel Salento"
VERSION = "0.1.0"


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(">>> Avvio applicazione")
    yield
    print(">>> Arresto applicazione")


app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    lifespan=lifespan,
)


@app.get("/", tags=["System"])
async def root():
    return {
        "application": APP_NAME,
        "version": VERSION,
        "status": "running",
    }


@app.get("/health", tags=["System"])
async def health():
    return {
        "status": "ok",
    }
