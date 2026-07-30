"""
Security Domain Schemas

CRM Vacanze Sicure nel Salento
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ==========================================================
# PROVIDER
# ==========================================================

class SecurityProviderBase(BaseModel):
    company_name: str = Field(..., max_length=200)
    contact_email: Optional[EmailStr] = None
    website: Optional[str] = None
    active: bool = True


class SecurityProviderCreate(SecurityProviderBase):
    pass


class SecurityProviderUpdate(BaseModel):
    company_name: Optional[str] = None
    contact_email: Optional[EmailStr] = None
    website: Optional[str] = None
    active: Optional[bool] = None


class SecurityProviderResponse(SecurityProviderBase):
    model_config = ConfigDict(from_attributes=True)

    uuid: UUID
    created_at: datetime
    updated_at: datetime


# ==========================================================
# INCIDENT
# ==========================================================

class SecurityIncidentBase(BaseModel):
    title: str
    description: str

    category: str
    severity: str

    event_start: Optional[date] = None
    event_end: Optional[date] = None
    notification_date: Optional[date] = None

    provider_uuid: Optional[UUID] = None

    gdpr_article33: bool = False
    gdpr_article34: bool = False


class SecurityIncidentCreate(SecurityIncidentBase):
    pass


class SecurityIncidentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    category: Optional[str] = None
    severity: Optional[str] = None
    status: Optional[str] = None

    event_start: Optional[date] = None
    event_end: Optional[date] = None
    notification_date: Optional[date] = None

    gdpr_article33: Optional[bool] = None
    gdpr_article34: Optional[bool] = None

    closed: Optional[bool] = None


class SecurityIncidentResponse(SecurityIncidentBase):

    model_config = ConfigDict(from_attributes=True)

    uuid: UUID
    incident_number: str
    status: str
    closed: bool

    created_at: datetime
    updated_at: datetime


# ==========================================================
# TIMELINE
# ==========================================================

class SecurityIncidentEventCreate(BaseModel):
    event_date: datetime
    title: str
    description: str


class SecurityIncidentEventResponse(SecurityIncidentEventCreate):

    model_config = ConfigDict(from_attributes=True)

    id: int


# ==========================================================
# ATTACHMENTS
# ==========================================================

class SecurityIncidentAttachmentResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    filename: str
    filepath: str
    mime_type: Optional[str]


# ==========================================================
# NOTIFICATIONS
# ==========================================================

class SecurityIncidentNotificationCreate(BaseModel):

    channel: str
    language: str
    recipients: int


class SecurityIncidentNotificationResponse(
    SecurityIncidentNotificationCreate
):

    model_config = ConfigDict(from_attributes=True)

    id: int
    sent_at: Optional[datetime]


# ==========================================================
# RISK ASSESSMENT
# ==========================================================

class SecurityRiskAssessmentCreate(BaseModel):

    personal_data: bool
    special_categories: bool

    high_risk: bool

    notify_authority: bool
    notify_data_subjects: bool

    notes: Optional[str] = None


class SecurityRiskAssessmentResponse(
    SecurityRiskAssessmentCreate
):

    model_config = ConfigDict(from_attributes=True)

    id: int


# ==========================================================
# COMPLETE INCIDENT
# ==========================================================

class SecurityIncidentDetail(SecurityIncidentResponse):

    provider: Optional[SecurityProviderResponse] = None

    timeline: list[SecurityIncidentEventResponse] = []

    notifications: list[
        SecurityIncidentNotificationResponse
    ] = []

    attachments: list[
        SecurityIncidentAttachmentResponse
    ] = []

    risk: Optional[
        SecurityRiskAssessmentResponse
    ] = None
