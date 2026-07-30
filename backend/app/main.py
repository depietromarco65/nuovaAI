from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.init_db import init_database

APP_NAME = "Vacanze Sicure nel Salento"
VERSION = "0.1.0"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Operazioni eseguite all'avvio e alla chiusura
    dell'applicazione.
    """

    print("=" * 60)
    print(f"Avvio di {APP_NAME}")
    print("=" * 60)

    # Inizializza il database
    init_database()

    print("Database inizializzato correttamente.")

    yield

    print("=" * 60)
    print(f"Arresto di {APP_NAME}")
    print("=" * 60)


app = FastAPI(
    title=APP_NAME,
    description="PMS + CRM + Booking Engine + AI per Vacanze Sicure nel Salento",
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


@app.get("/info", tags=["System"])
async def info():
    return {
        "application": APP_NAME,
        "version": VERSION,
        "environment": "development",
        "database": "SQLite",
        "framework": "FastAPI",
    }
