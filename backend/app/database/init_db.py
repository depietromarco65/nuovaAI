from app.database.base import Base
from app.database.session import engine

# ==========================================================
# IMPORT DI TUTTI I MODELLI
# ==========================================================
# Ogni nuovo modello dovrà essere importato qui
# affinché SQLAlchemy lo registri in Base.metadata.
#
# Esempio:
#
# from app.models.user import User
# from app.models.guest import Guest
# from app.models.booking import Booking
#
# ==========================================================


def init_database() -> None:
    """
    Crea tutte le tabelle registrate in Base.metadata.

    In fase di sviluppo utilizziamo create_all().
    In produzione la gestione sarà affidata ad Alembic.
    """

    Base.metadata.create_all(bind=engine)
