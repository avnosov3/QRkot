from datetime import datetime
from typing import List

from app.crud.base import ModelType


def investment_procces(
    target: ModelType, sources: List[ModelType]
) -> List[ModelType]:
    target.invested_amount = (
        0 if target.invested_amount is None else target.invested_amount
    )
    new_sources = []
    for source in sources:
        if target.fully_invested:
            break
        donation = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount
        )
        for obj in (target, source):
            obj.invested_amount += donation
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = 1
                obj.close_date = datetime.utcnow()
        new_sources.append(source)
    return new_sources
