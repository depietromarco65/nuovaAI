"""
Security Domain Models

CRM Vacanze Sicure nel Salento

Gestione degli incidenti di sicurezza,
adempimenti GDPR,
audit e comunicazioni.
"""

from __future__ import annotations

import uuid

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin


# ==========================================================
# ENUM
# ==========================================================

INCIDENT_STATUS = (
    "OPEN",
    "MONITORING",
    "CLOSED",
)

INCIDENT_SEVERITY = (
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
)

INCIDENT_CATEGORY = (
    "DATA_BREACH",
    "PHISHING",
    "SMISHING",
    "VISHING",
    "MALWARE",
    "RANSOMWARE",
    "TOKEN_COMPROMISE",
    "SOFTWARE_VULNERABILITY",
    "UNAUTHORIZED_ACCESS",
    "OTHER",
)


# ==========================================================
# SECURITY PROVIDER
# ==========================================================


class SecurityProvider(Base, TimestampMixin):

    __tablename__ = "security_providers"

    id: Mapped[int] = mapped_column(primary_key=True)

    uuid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    company_name: Mapped[str] = mapped_column(String(200))

    contact_email: Mapped[str | None] = mapped_column(String(255))

    website: Mapped[str | None] = mapped_column(String(255))

    active: Mapped[bool] = mapped_column(Boolean, default=True)

    incidents = relationship(
        "SecurityIncident",
        back_populates="provider",
    )


# ==========================================================
# SECURITY INCIDENT
# ==========================================================


class SecurityIncident(Base, TimestampMixin):

    __tablename__ = "security_incidents"

    id: Mapped[int] = mapped_column(primary_key=True)

    uuid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    incident_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
    )

    title: Mapped[str] = mapped_column(
        String(300),
    )

    description: Mapped[str] = mapped_column(
        Text,
    )

    category: Mapped[str] = mapped_column(
        Enum(*INCIDENT_CATEGORY, name="incident_category"),
    )

    severity: Mapped[str] = mapped_column(
        Enum(*INCIDENT_SEVERITY, name="incident_severity"),
    )

    status: Mapped[str] = mapped_column(
        Enum(*INCIDENT_STATUS, name="incident_status"),
        default="OPEN",
    )

    event_start: Mapped[Date | None]

    event_end: Mapped[Date | None]

    notification_date: Mapped[Date | None]

    provider_id: Mapped[int | None] = mapped_column(
        ForeignKey("security_providers.id")
    )

    gdpr_article33: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    gdpr_article34: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    closed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    provider = relationship(
        "SecurityProvider",
        back_populates="incidents",
    )

    timeline = relationship(
        "SecurityIncidentEvent",
        cascade="all, delete-orphan",
        back_populates="incident",
    )

    attachments = relationship(
        "SecurityIncidentAttachment",
        cascade="all, delete-orphan",
        back_populates="incident",
    )

    notifications = relationship(
        "SecurityIncidentNotification",
        cascade="all, delete-orphan",
        back_populates="incident",
    )

    guests = relationship(
        "SecurityIncidentAffectedGuest",
        cascade="all, delete-orphan",
        back_populates="incident",
    )

    risk = relationship(
        "SecurityRiskAssessment",
        uselist=False,
        back_populates="incident",
    )


# ==========================================================
# TIMELINE
# ==========================================================


class SecurityIncidentEvent(Base, TimestampMixin):

    __tablename__ = "security_incident_events"

    id: Mapped[int] = mapped_column(primary_key=True)

    incident_id: Mapped[int] = mapped_column(
        ForeignKey("security_incidents.id")
    )

    event_date: Mapped[DateTime]

    title: Mapped[str] = mapped_column(
        String(200),
    )

    description: Mapped[str] = mapped_column(
        Text,
    )

    incident = relationship(
        "SecurityIncident",
        back_populates="timeline",
    )


# ==========================================================
# ATTACHMENTS
# ==========================================================


class SecurityIncidentAttachment(Base, TimestampMixin):

    __tablename__ = "security_incident_attachments"

    id: Mapped[int] = mapped_column(primary_key=True)

    incident_id: Mapped[int] = mapped_column(
        ForeignKey("security_incidents.id")
    )

    filename: Mapped[str] = mapped_column(
        String(255),
    )

    filepath: Mapped[str] = mapped_column(
        String(500),
    )

    mime_type: Mapped[str | None] = mapped_column(
        String(100),
    )

    incident = relationship(
        "SecurityIncident",
        back_populates="attachments",
    )


# ==========================================================
# NOTIFICATIONS
# ==========================================================


class SecurityIncidentNotification(Base, TimestampMixin):

    __tablename__ = "security_incident_notifications"

    id: Mapped[int] = mapped_column(primary_key=True)

    incident_id: Mapped[int] = mapped_column(
        ForeignKey("security_incidents.id")
    )

    channel: Mapped[str] = mapped_column(
        String(30),
    )

    language: Mapped[str] = mapped_column(
        String(5),
    )

    recipients: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    sent_at: Mapped[DateTime | None]

    incident = relationship(
        "SecurityIncident",
        back_populates="notifications",
    )


# ==========================================================
# AFFECTED GUESTS
# ==========================================================


class SecurityIncidentAffectedGuest(Base, TimestampMixin):

    __tablename__ = "security_incident_guests"

    id: Mapped[int] = mapped_column(primary_key=True)

    incident_id: Mapped[int] = mapped_column(
        ForeignKey("security_incidents.id")
    )

    guest_uuid: Mapped[uuid.UUID]

    notification_sent: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    incident = relationship(
        "SecurityIncident",
        back_populates="guests",
    )


# ==========================================================
# RISK ASSESSMENT
# ==========================================================


class SecurityRiskAssessment(Base, TimestampMixin):

    __tablename__ = "security_risk_assessments"

    id: Mapped[int] = mapped_column(primary_key=True)

    incident_id: Mapped[int] = mapped_column(
        ForeignKey("security_incidents.id"),
        unique=True,
    )

    personal_data: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    special_categories: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    high_risk: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    notify_authority: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    notify_data_subjects: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
    )

    incident = relationship(
        "SecurityIncident",
        back_populates="risk",
    )
