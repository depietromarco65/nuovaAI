from .models import Tenant
from .repository import TenantRepository


class TenantService:

    def __init__(self, repository: TenantRepository):
        self.repository = repository

    async def create(self, data):

        tenant = Tenant(**data.model_dump())

        return await self.repository.create(tenant)

    async def list(self):

        return await self.repository.get_all()

    async def get(self, tenant_id):

        return await self.repository.get_by_id(tenant_id)
