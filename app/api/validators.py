
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_crud

UNIQUE_MESSAGE = 'Проект с таким именем уже существует!'
PROJECT_NOT_FOUND = 'Проект не найден'


async def check_name_duplicate(
    name: str,
    session: AsyncSession
):
    if await charity_crud.exists_project_by_name(name, session):
        raise HTTPException(
            status_code=400,
            detail=UNIQUE_MESSAGE
        )


async def check_project_exists_by_id(
    id: int,
    sesssion: AsyncSession
):
    project = await charity_crud.get(id, sesssion)
    if project is None:
        raise HTTPException(
            status_code=404,
            detail=PROJECT_NOT_FOUND
        )
    return project
