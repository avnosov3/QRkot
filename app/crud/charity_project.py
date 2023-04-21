from typing import Optional

from sqlalchemy import select

from app.crud.base import AsyncSession, CRUDBase, ModelType
from app.models.charity_project import CharityProject

FORBIDDEN_TO_INVEST = 'Закрытый проект нельзя редактировать!'


class CharityCRUD(CRUDBase):

    async def exists_project_by_name(
        self,
        name: str,
        session: AsyncSession,
    ) -> Optional[ModelType]:
        project = await session.scalars(
            select(True).where(
                select(CharityProject).where(
                    CharityProject.name == name
                ).exists()
            )
        )
        return project.first()


charity_crud = CharityCRUD(CharityProject)
