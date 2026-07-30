import logging
import sys

from app.core.config import settings


def setup_logging() -> None:
    """
    Configura il sistema di logging dell'applicazione.
    """

    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )


def get_logger(name: str) -> logging.Logger:
    """
    Restituisce un logger configurato.
    """

    return logging.getLogger(name)
