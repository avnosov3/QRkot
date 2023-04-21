from fastapi import FastAPI

from app.api.routers import main_router_v1
from app.core.init_db import create_first_superuser

TITLE = 'Благотворительный фонд поддержки'

app = FastAPI(title=TITLE)

app.include_router(main_router_v1)


@app.on_event('startup')
async def startup():
    await create_first_superuser()
