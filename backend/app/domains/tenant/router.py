from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db

from .repository import TenantRepository
from .schemas import (
    TenantCreate,
    TenantResponse,
    TenantUpdate,
)
from .service import TenantService

router = APIRouter(
    prefix="/tenants",
    tags=["Tenants"],
)


def get_service(db: AsyncSession = Depends(get_db)) -> TenantService:
    return TenantService(TenantRepository(db))


@router.get(
    "/",
    response_model=list[TenantResponse],
)
async def list_tenants(
    service: TenantService = Depends(get_service),
):
    return await service.list()


@router.get(
    "/{tenant_id}",
    response_model=TenantResponse,
)
async def get_tenant(
    tenant_id: UUID,
    service: TenantService = Depends(get_service),
):
    tenant = await service.get(tenant_id)

    if tenant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant not found",
        )

    return tenant


@router.post(
    "/",
    response_model=TenantResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_tenant(
    tenant: TenantCreate,
    service: TenantService = Depends(get_service),
):
    try:
        return await service.create(tenant)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e),
        )


@router.put(
    "/{tenant_id}",
    response_model=TenantResponse,
)
async def update_tenant(
    tenant_id: UUID,
    tenant: TenantUpdate,
    service: TenantService = Depends(get_service),
):
    try:
        return await service.update(
            tenant_id,
            tenant,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/{tenant_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_tenant(
    tenant_id: UUID,
    service: TenantService = Depends(get_service),
):
    try:
        await service.delete(tenant_id)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
