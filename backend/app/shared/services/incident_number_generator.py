"""
Incident Number Generator

CRM Vacanze Sicure nel Salento
"""

from __future__ import annotations

from datetime import datetime


class IncidentNumberGenerator:
    """
    Genera il numero identificativo di un incidente di sicurezza.

    Formato:

    SEC-{PROVIDER}-{ORIGIN}-{YEAR}-{PROGRESSIVE}

    esempio:

    SEC-OCT-TK-2026-0001
    """

    PREFIX = "SEC"

    def generate(
        self,
        provider_code: str,
        origin_code: str,
        progressive: int,
        year: int | None = None,
    ) -> str:

        if year is None:
            year = datetime.now().year

        provider_code = provider_code.upper().strip()
        origin_code = origin_code.upper().strip()

        return (
            f"{self.PREFIX}-"
            f"{provider_code}-"
            f"{origin_code}-"
            f"{year}-"
            f"{progressive:04d}"
        )
