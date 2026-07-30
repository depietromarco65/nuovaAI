"""
Security Service

CRM Vacanze Sicure nel Salento
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from app.domains.security.models import SecurityIncident
from app.domains.security.repositories.incident_repository import (
    SecurityIncidentRepository,
)
from app.domains.security.schemas import (
    SecurityIncidentCreate,
    SecurityIncidentUpdate,
)


class SecurityService:

    def __init__(
        self,
        repository: SecurityIncidentRepository,
    ):
        self.repository = repository

    # =====================================================
    # CREATE
    # =====================================================

    def create_incident(
        self,
        data: SecurityIncidentCreate,
    ) -> SecurityIncident:

        incident = SecurityIncident()

        incident.incident_number = self._generate_number()

        incident.title = data.title
        incident.description = data.description

        incident.category = data.category
        incident.severity = data.severity

        incident.event_start = data.event_start
        incident.event_end = data.event_end
        incident.notification_date = data.notification_date

        incident.gdpr_article33 = data.gdpr_article33
        incident.gdpr_article34 = data.gdpr_article34

        incident.status = "OPEN"
        incident.closed = False

        return self.repository.create(incident)

    # =====================================================
    # READ
    # =====================================================

    def get_incident(
        self,
        incident_uuid: UUID,
    ) -> SecurityIncident | None:

        return self.repository.get_by_uuid(
            incident_uuid
        )

    def list_incidents(self):

        return self.repository.list()

    # =====================================================
    # UPDATE
    # =====================================================

    def update_incident(
        self,
        incident: SecurityIncident,
        data: SecurityIncidentUpdate,
    ) -> SecurityIncident:

        payload = data.model_dump(
            exclude_unset=True
        )

        for field, value in payload.items():
            setattr(
                incident,
                field,
                value,
            )

        return self.repository.update(
            incident
        )

    # =====================================================
    # CLOSE
    # =====================================================

    def close_incident(
        self,
        incident: SecurityIncident,
    ) -> SecurityIncident:

        incident.closed = True
        incident.status = "CLOSED"

        return self.repository.update(
            incident
        )

    # =====================================================
    # REOPEN
    # =====================================================

    def reopen_incident(
        self,
        incident: SecurityIncident,
    ) -> SecurityIncident:

        incident.closed = False
        incident.status = "OPEN"

        return self.repository.update(
            incident
        )

    # =====================================================
    # PRIVATE
    # =====================================================

    def _generate_number(self) -> str:

        year = datetime.now().year

        # Da sostituire con contatore persistente
        progressive = 1

        return f"INC-{year}-{progressive:04d}"
