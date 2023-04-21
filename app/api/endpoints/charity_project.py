from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_name_duplicate, check_project_exists_by_id
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_crud
from app.crud.donation import donation_crud
from app.schemas.charity_project import CharityCreate, CharityDB, CharityUpdate
from app.services.investment_procces import investment_procces

router = APIRouter()

PROJECTS_NOT_FOUND = 'Созданные проекты не найдены'
FORBIDDEN_TO_CHANGE = 'Закрытый проект нельзя редактировать!'
FORBIDDEN_TO_DELETE = 'В проект были внесены средства, не подлежит удалению!'


@router.get(
    '/',
    response_model=List[CharityDB],
    response_model_exclude_none=True
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session)
):
    projects = await charity_crud.get_all(session)
    if projects is None:
        raise HTTPException(
            status_code=404,
            detail=PROJECTS_NOT_FOUND
        )
    return projects


@router.post(
    '/',
    response_model=CharityDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def create_charity_project(
    charity_project: CharityCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(charity_project.name, session)
    project = await charity_crud.create(charity_project, session, commit=False)
    session.add_all(
        investment_procces(
            target=project,
            sources=await donation_crud.get_not_invested(session)
        )
    )
    await session.commit()
    await session.refresh(project)
    return project


@router.patch(
    '/{project_id}',
    response_model=CharityDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_charity_project(
    project_id: int,
    charity_project: CharityUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    project = await check_project_exists_by_id(project_id, session)
    if project.fully_invested:
        raise HTTPException(
            status_code=400,
            detail=FORBIDDEN_TO_CHANGE
        )
    name = charity_project.name
    if charity_project.name is not None:
        await check_name_duplicate(name, session)
    return await charity_crud.update(project, charity_project, session)


@router.delete(
    '/{project_id}',
    response_model=CharityDB,
    dependencies=[Depends(current_superuser)]
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    project = await check_project_exists_by_id(project_id, session)
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail=FORBIDDEN_TO_DELETE
        )
    return await charity_crud.delete(project, session)
