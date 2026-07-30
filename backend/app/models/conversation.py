from sqlalchemy import String, Text

from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.database.mixins import BaseMixin


class Conversation(BaseMixin, Base):
    __tablename__ = "conversations"

    subject: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    channel: Mapped[str] = mapped_column(
        String(30),
        default="EMAIL",
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="OPEN",
    )

    category: Mapped[str] = mapped_column(
        String(50),
        default="GENERAL",
    )

    description: Mapped[str] = mapped_column(
        Text,
    )
