from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Tenant


class TenantRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Tenant]:
        result = await self.db.execute(
            select(Tenant).order_by(Tenant.company_name)
        )
        return result.scalars().all()

    async def get_by_id(self, tenant_id: UUID) -> Tenant | None:
        return await self.db.get(Tenant, tenant_id)

    async def get_by_code(self, code: str) -> Tenant | None:
        result = await self.db.execute(
            select(Tenant).where(Tenant.code == code)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Tenant | None:
        result = await self.db.execute(
            select(Tenant).where(Tenant.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, tenant: Tenant) -> Tenant:
        self.db.add(tenant)
        await self.db.commit()
        await self.db.refresh(tenant)
        return tenant

    async def update(self, tenant: Tenant) -> Tenant:
        await self.db.commit()
        await self.db.refresh(tenant)
        return tenant

    async def delete(self, tenant: Tenant) -> None:
        await self.db.delete(tenant)
        await self.db.commit()
