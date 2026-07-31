op.create_table(
    "tenants",

    sa.Column(
        "id",
        postgresql.UUID(as_uuid=True),
        primary_key=True
    ),

    sa.Column(
        "code",
        sa.String(30),
        nullable=False,
        unique=True
    ),

    sa.Column(
        "company_name",
        sa.String(150),
        nullable=False
    ),

    sa.Column(
        "vat_number",
        sa.String(30)
    ),

    sa.Column(
        "tax_code",
        sa.String(30)
    ),

    sa.Column(
        "email",
        sa.String(150),
        nullable=False,
        unique=True
    ),

    sa.Column(
        "phone",
        sa.String(50)
    ),

    sa.Column(
        "website",
        sa.String(255)
    ),

    sa.Column(
        "status",
        sa.String(20),
        nullable=False,
        server_default="ACTIVE"
    ),

    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=sa.func.now()
    ),

    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        server_default=sa.func.now()
    )
)
