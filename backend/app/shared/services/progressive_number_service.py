"""
Progressive Number Service

CRM Vacanze Sicure nel Salento

Servizio centralizzato per la generazione dei numeri
progressivi del sistema.

Tutti i documenti ufficiali del CRM devono utilizzare
questo servizio.
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import Session

from app.shared.models.system_counter import SystemCounter


class ProgressiveNumberService:
    """
    Gestisce i contatori progressivi del sistema.

    Esempi:

    SEC-2026-0001
    BOOK-2026-000123
    INV-2026-000045
    """

    def __init__(self, db: Session):
        self.db = db

    # =====================================================
    # NEXT PROGRESSIVE
    # =====================================================

    def next(
        self,
        code: str,
        year: int | None = None,
    ) -> int:
        """
        Restituisce il prossimo progressivo disponibile
        per il codice richiesto.
        """

        if year is None:
            year = datetime.now().year

        counter = (
            self.db.query(SystemCounter)
            .filter(
                SystemCounter.code == code,
                SystemCounter.year == year,
            )
            .first()
        )

        if counter is None:

            counter = SystemCounter(
                code=code,
                year=year,
                last_value=1,
            )

            self.db.add(counter)
            self.db.commit()

            return 1

        counter.last_value += 1

        self.db.commit()

        return counter.last_value

    # =====================================================
    # CURRENT VALUE
    # =====================================================

    def current(
        self,
        code: str,
        year: int | None = None,
    ) -> int:

        if year is None:
            year = datetime.now().year

        counter = (
            self.db.query(SystemCounter)
            .filter(
                SystemCounter.code == code,
                SystemCounter.year == year,
            )
            .first()
        )

        if counter is None:
            return 0

        return counter.last_value

    # =====================================================
    # RESET
    # =====================================================

    def reset(
        self,
        code: str,
        year: int,
    ) -> None:

        counter = (
            self.db.query(SystemCounter)
            .filter(
                SystemCounter.code == code,
                SystemCounter.year == year,
            )
            .first()
        )

        if counter is None:
            return

        counter.last_value = 0

        self.db.commit()
