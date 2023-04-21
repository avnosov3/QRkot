from fastapi import APIRouter

from app.api.endpoints import (
    charity_router, donation_router, google_router, user_router
)

main_router_v1 = APIRouter()
main_router_v1.include_router(
    charity_router,
    prefix='/charity_project',
    tags=['Проекты благотворительности']
)
main_router_v1.include_router(
    donation_router,
    prefix='/donation',
    tags=['Пожертвования']
)
main_router_v1.include_router(
    google_router,
    prefix='/google',
    tags=['Google']
)
main_router_v1.include_router(user_router)
