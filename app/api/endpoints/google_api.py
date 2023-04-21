from typing import List

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.crud.charity_project import charity_crud
from app.services.google_api import spreadsheets_create
from app.schemas.charity_project import CharityDB


router = APIRouter()


@router.get(
    '/',
    response_model=List[CharityDB],
    response_model_exclude_none=True
)
async def get_all_invested(
    session: AsyncSession = Depends(get_async_session),
    wrapper_servises: Aiogoogle = Depends(get_service)
):
    await spreadsheets_create(wrapper_servises)
    return await charity_crud.get_projects_by_completion_rate(session)
