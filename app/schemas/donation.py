from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt

from app.schemas.mixins import CharityDonationMixin


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]


class DonationCreateResponse(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationGetAllResponse(CharityDonationMixin, DonationCreate):
    user_id: Optional[int]

    class Config:
        orm_mode = True
