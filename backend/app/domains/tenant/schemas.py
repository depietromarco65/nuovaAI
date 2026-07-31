from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class TenantBase(BaseModel):
    code: str = Field(..., max_length=30)
    company_name: str = Field(..., max_length=150)
    vat_number: str | None = Field(default=None, max_length=30)
    tax_code: str | None = Field(default=None, max_length=30)
    email: EmailStr
    phone: str | None = Field(default=None, max_length=50)
    website: str | None = Field(default=None, max_length=255)


class TenantCreate(TenantBase):
    pass


class TenantUpdate(BaseModel):
    company_name: str | None = Field(default=None, max_length=150)
    vat_number: str | None = Field(default=None, max_length=30)
    tax_code: str | None = Field(default=None, max_length=30)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=50)
    website: str | None = Field(default=None, max_length=255)
    status: str | None = Field(default=None, max_length=20)


class TenantResponse(TenantBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
