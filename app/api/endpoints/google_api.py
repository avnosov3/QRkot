from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity_project import charity_crud
from app.schemas.charity_project import CharityDB


router = APIRouter()


@router.get(
    '/',
    response_model=List[CharityDB],
    response_model_exclude_none=True
)
async def get_all_invested(
    session: AsyncSession = Depends(get_async_session)
):
    return await charity_crud.get_projects_by_completion_rate(session)
