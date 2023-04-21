from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

from app.schemas.mixins import CharityDonationMixin


class CharityBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str = Field(...)

    class Config:
        min_anystr_length = 1


class CharityDB(CharityDonationMixin, CharityBase):
    description: str

    class Config:
        orm_mode = True


class CharityCreate(CharityBase):
    full_amount: PositiveInt


class CharityUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1
