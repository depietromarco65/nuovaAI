from fastapi import APIRouter, Depends

from app.database.session import get_db

from .schemas import (
    TenantCreate,
    TenantResponse
)

from .repository import TenantRepository
from .service import TenantService

router = APIRouter(
    prefix="/tenants",
    tags=["Tenants"]
)


@router.get(
    "/",
    response_model=list[TenantResponse]
)
async def list_tenants(db=Depends(get_db)):

    service = TenantService(
        TenantRepository(db)
    )

    return await service.list()


@router.post(
    "/",
    response_model=TenantResponse
)
async def create_tenant(
        tenant: TenantCreate,
        db=Depends(get_db)
):

    service = TenantService(
        TenantRepository(db)
    )

    return await service.create(tenant)
