from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core.db import Base


class InvestmentDate(Base):
    __abstract__ = True
    __table_args__ = (CheckConstraint('0 <= invested_amount <= full_amount'),)

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    close_date = Column(DateTime)

    OUT = (
        'пожертвовали {invested} из {full} '
        'статус {status} '
        'дата открытия {create_date} '
        'дата закрытия {close_date} '
    )

    def __repr__(self):
        return self.OUT.format(
            invested=self.invested_amount, full=self.full_amount,
            status=self.fully_invested, create_date=self.create_date,
            close_date=self.close_date
        )
