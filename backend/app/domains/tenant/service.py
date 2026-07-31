from uuid import UUID

from .models import Tenant
from .repository import TenantRepository


class TenantService:

    def __init__(self, repository: TenantRepository):
        self.repository = repository

    async def create(self, data):

        # Verifica codice già esistente
        existing = await self.repository.get_by_code(data.code)

        if existing:
            raise ValueError("Tenant code already exists.")

        # Verifica email già esistente
        existing = await self.repository.get_by_email(data.email)

        if existing:
            raise ValueError("Email already exists.")

        tenant = Tenant(**data.model_dump())

        return await self.repository.create(tenant)

    async def list(self):

        return await self.repository.get_all()

    async def get(self, tenant_id: UUID):

        return await self.repository.get_by_id(tenant_id)

    async def update(self, tenant_id: UUID, data):

        tenant = await self.repository.get_by_id(tenant_id)

        if tenant is None:
            raise ValueError("Tenant not found.")

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(tenant, field, value)

        return await self.repository.update(tenant)

    async def delete(self, tenant_id: UUID):

        tenant = await self.repository.get_by_id(tenant_id)

        if tenant is None:
            raise ValueError("Tenant not found.")

        await self.repository.delete(tenant)
