from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import (
    Base,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
)


class Tenant(
    Base,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    __tablename__ = "tenants"

    code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    company_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    vat_number: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    tax_code: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE",
        nullable=False,
    )
