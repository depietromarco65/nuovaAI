from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Tenant


class TenantRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):

        result = await self.db.execute(
            select(Tenant)
        )

        return result.scalars().all()

    async def get_by_id(self, tenant_id):

        return await self.db.get(Tenant, tenant_id)

    async def create(self, tenant):

        self.db.add(tenant)

        await self.db.commit()

        await self.db.refresh(tenant)

        return tenant
