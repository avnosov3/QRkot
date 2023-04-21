from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    database_url: str = 'sqlite+aiosqlite:///./cat_charity_fund.db'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()