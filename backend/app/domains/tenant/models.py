from uuid import uuid4
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True
    )

    company_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    vat_number: Mapped[str | None] = mapped_column(
        String(30)
    )

    tax_code: Mapped[str | None] = mapped_column(
        String(30)
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(50)
    )

    website: Mapped[str | None] = mapped_column(
        String(255)
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE"
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
