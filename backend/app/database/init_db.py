from app.database.base import Base
from app.database.session import engine

# importa tutti i modelli
from app.models.conversation import Conversation  # noqa


def init_database():
    Base.metadata.create_all(bind=engine)
