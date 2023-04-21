from typing import Optional

from sqlalchemy import select, func

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

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ):
        projects = await session.scalars(
            select(CharityProject).where(
                CharityProject.fully_invested == 1
            ).order_by(
                func.julianday(CharityProject.close_date) -
                func.julianday(CharityProject.create_date)
            )
        )
        return projects.all()


charity_crud = CharityCRUD(CharityProject)
