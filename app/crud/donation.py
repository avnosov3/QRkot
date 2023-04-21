from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.donation import Donation
from app.models.user import User


class DonationCRUD(CRUDBase):

    async def get_user_donations(
        self,
        user: User,
        session: AsyncSession
    ):
        donations = await session.scalars(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.all()


donation_crud = DonationCRUD(Donation)
