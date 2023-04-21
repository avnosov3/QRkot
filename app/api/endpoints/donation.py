from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_crud
from app.crud.donation import donation_crud
from app.models.user import User
from app.schemas.donation import (
    DonationCreate, DonationCreateResponse, DonationGetAllResponse
)
from app.services.investment_procces import investment_procces

router = APIRouter()

DONATIONS_NOT_FOUND = 'Созданные пожертвования не найдены'


@router.get(
    '/',
    response_model=List[DonationGetAllResponse],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    donations = await donation_crud.get_all(session)
    if donations is None:
        raise HTTPException(
            status_code=404,
            detail=DONATIONS_NOT_FOUND
        )
    return donations


@router.get(
    '/my',
    response_model=List[DonationCreateResponse],
    dependencies=[Depends(current_user)]
)
async def get_user_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    return await donation_crud.get_user_donations(user, session)


@router.post(
    '/',
    response_model=DonationCreateResponse,
    response_model_exclude_none=True,
    dependencies=[Depends(current_user)],
)
async def create_donation(
    donation: DonationCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    new_donation = await donation_crud.create(donation, session, user, False)
    session.add_all(
        investment_procces(
            target=new_donation,
            sources=await charity_crud.get_not_invested(session)
        )
    )
    await session.commit()
    await session.refresh(new_donation)
    return new_donation
