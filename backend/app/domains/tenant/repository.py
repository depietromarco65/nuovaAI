from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Tenant


class TenantRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Tenant]:
        """
        Restituisce l'elenco di tutti i tenant.
        """
        result = await self.db.execute(
            select(Tenant).order_by(Tenant.company_name)
        )

        return result.scalars().all()

    async def get_by_id(self, tenant_id: UUID) -> Tenant | None:
        """
        Restituisce un tenant tramite ID.
        """
        return await self.db.get(Tenant, tenant_id)

    async def get_by_code(self, code: str) -> Tenant | None:
        """
        Cerca un tenant tramite il codice univoco.
        """
        result = await self.db.execute(
            select(Tenant).where(Tenant.code == code)
        )

        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Tenant | None:
        """
        Cerca un tenant tramite email.
        """
        result = await self.db.execute(
            select(Tenant).where(Tenant.email == email)
        )

        return result.scalar_one_or_none()

    async def create(self, tenant: Tenant) -> Tenant:
        """
        Crea un nuovo tenant.
        """
        self.db.add(tenant)

        await self.db.commit()

        await self.db.refresh(tenant)

        return tenant

    async def update(self, tenant: Tenant) -> Tenant:
        """
        Aggiorna un tenant esistente.
        """
        await self.db.commit()

        await self.db.refresh(tenant)

        return tenant

    async def delete(self, tenant: Tenant) -> None:
        """
        Elimina definitivamente un tenant.
        In futuro sarà sostituito dal Soft Delete.
        """
        await self.db.delete(tenant)

        await self.db.commit()
