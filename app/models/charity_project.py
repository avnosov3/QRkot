from sqlalchemy import Column, String, Text

from app.models.investment_date import InvestmentDate


class CharityProject(InvestmentDate):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    OUT_PROJECT = 'В фонд {name:.15} {base}'

    def __repr__(self):
        return self.OUT_PROJECT.format(
            name=self.name, base=super().__repr__()
        )
