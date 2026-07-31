"""Create tenants table"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revision identifiers
revision: str = "20260731_create_tenants"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tenants",

        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False
        ),

        sa.Column(
            "code",
            sa.String(length=30),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "company_name",
            sa.String(length=150),
            nullable=False
        ),

        sa.Column(
            "vat_number",
            sa.String(length=30),
            nullable=True
        ),

        sa.Column(
            "tax_code",
            sa.String(length=30),
            nullable=True
        ),

        sa.Column(
            "email",
            sa.String(length=150),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "phone",
            sa.String(length=50),
            nullable=True
        ),

        sa.Column(
            "website",
            sa.String(length=255),
            nullable=True
        ),

        sa.Column(
            "status",
            sa.String(length=20),
            nullable=False,
            server_default=sa.text("'ACTIVE'")
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now()
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now()
        ),
    )

    op.create_index(
        "ix_tenants_code",
        "tenants",
        ["code"],
        unique=True,
    )

    op.create_index(
        "ix_tenants_email",
        "tenants",
        ["email"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_tenants_email", table_name="tenants")
    op.drop_index("ix_tenants_code", table_name="tenants")
    op.drop_table("tenants")
