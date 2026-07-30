"""
System Counter Model

CRM Vacanze Sicure nel Salento

Gestisce tutti i contatori progressivi del sistema.
"""

from __future__ import annotations

import uuid

from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.database.mixins import TimestampMixin


class SystemCounter(Base, TimestampMixin):
    """
    Contatore progressivo del sistema.

    Ogni combinazione (code, year) mantiene
    l'ultimo numero assegnato.

    Esempi:

    code = "SEC-OCT-TK"
    year = 2026
    last_value = 15

    prossimo numero:

    SEC-OCT-TK-2026-0016
    """

    __tablename__ = "system_counters"

    __table_args__ = (
        UniqueConstraint(
            "code",
            "year",
            name="uq_system_counter_code_year",
        ),
    )

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    uuid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    # =====================================================
    # COUNTER
    # =====================================================

    code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
        comment="Codice del contatore (es. SEC-OCT-TK)",
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True,
        comment="Anno del contatore",
    )

    last_value: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        comment="Ultimo progressivo assegnato",
    )

    # =====================================================
    # DESCRIPTION
    # =====================================================

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="Descrizione del contatore",
    )

    # =====================================================
    # METHODS
    # =====================================================

    def __repr__(self) -> str:
        return (
            f"<SystemCounter("
            f"code='{self.code}', "
            f"year={self.year}, "
            f"last_value={self.last_value}"
            f")>"
        )
