from fastapi import APIRouter
from app.api.endpoints import user_router, order_router

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(order_router, tags=["Заказы"])
