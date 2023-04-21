from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class CharityDonationMixin(BaseModel):
    full_amount: Optional[PositiveInt]
    id: Optional[int]
    invested_amount: Optional[int] = 0
    fully_invested: Optional[bool] = False
    create_date: Optional[datetime]
    close_date: Optional[datetime]
