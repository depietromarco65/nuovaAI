"""
Security Incident Repository

CRM Vacanze Sicure nel Salento
"""

from __future__ import annotations

from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domains.security.models import SecurityIncident


class SecurityIncidentRepository:

    def __init__(self, db: Session):
        self.db = db

    # =====================================================
    # CREATE
    # =====================================================

    def create(
        self,
        incident: SecurityIncident,
    ) -> SecurityIncident:

        self.db.add(incident)
        self.db.commit()
        self.db.refresh(incident)

        return incident

    # =====================================================
    # READ
    # =====================================================

    def get_by_uuid(
        self,
        incident_uuid: UUID,
    ) -> SecurityIncident | None:

        stmt = (
            select(SecurityIncident)
            .where(SecurityIncident.uuid == incident_uuid)
        )

        return self.db.scalar(stmt)

    def get_by_number(
        self,
        incident_number: str,
    ) -> SecurityIncident | None:

        stmt = (
            select(SecurityIncident)
            .where(
                SecurityIncident.incident_number
                == incident_number
            )
        )

        return self.db.scalar(stmt)

    def list(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> Sequence[SecurityIncident]:

        stmt = (
            select(SecurityIncident)
            .offset(offset)
            .limit(limit)
            .order_by(SecurityIncident.created_at.desc())
        )

        return self.db.scalars(stmt).all()

    # =====================================================
    # UPDATE
    # =====================================================

    def update(
        self,
        incident: SecurityIncident,
    ) -> SecurityIncident:

        self.db.add(incident)
        self.db.commit()
        self.db.refresh(incident)

        return incident

    # =====================================================
    # DELETE
    # =====================================================

    def delete(
        self,
        incident: SecurityIncident,
    ) -> None:

        self.db.delete(incident)
        self.db.commit()

    # =====================================================
    # STATUS
    # =====================================================

    def open_incidents(
        self,
    ) -> Sequence[SecurityIncident]:

        stmt = (
            select(SecurityIncident)
            .where(SecurityIncident.closed.is_(False))
            .order_by(SecurityIncident.created_at.desc())
        )

        return self.db.scalars(stmt).all()

    def closed_incidents(
        self,
    ) -> Sequence[SecurityIncident]:

        stmt = (
            select(SecurityIncident)
            .where(SecurityIncident.closed.is_(True))
            .order_by(SecurityIncident.created_at.desc())
        )

        return self.db.scalars(stmt).all()
