from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class TenantCreate(BaseModel):
    code: str
    company_name: str
    vat_number: str | None = None
    tax_code: str | None = None
    email: EmailStr
    phone: str | None = None
    website: str | None = None


class TenantUpdate(BaseModel):
    company_name: str | None = None
    vat_number: str | None = None
    tax_code: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    website: str | None = None
    status: str | None = None


class TenantResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    code: str
    company_name: str
    email: EmailStr
    status: str
    created_at: datetime
