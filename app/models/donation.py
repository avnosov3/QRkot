from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.investment_date import InvestmentDate


class Donation(InvestmentDate):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    OUT_DONATION = 'Пользователь {user_id} {base}'

    def __repr__(self):
        return self.OUT_DONATION.format(
            user_id=self.user_id,
            base=super().__repr__()
        )
