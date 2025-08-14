from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models.order import Order
from app.schemas.order import OrderRead, OrderCreate
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.models import User

from app.crud import order_crud


router = APIRouter()


@router.get(
    '/orders',
    response_model=List[OrderRead],
)
async def get_all_my_orders(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    orders = await order_crud.get_multi(
        session,
        Order.user_id == user.id,
    )
    return orders


@router.post(
    '/orders',
    response_model=OrderRead,
)
async def create_orders(
        order: OrderCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    new_order = await order_crud.create(
        obj_in=order.dict(),
        session=session,
        user=user,
    )
    return new_order


@router.patch(
    '/orders/{order_id}',
    response_model=OrderRead,
)
async def update_orders(
        order_id: int,
        order: OrderCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    db_order = await order_crud.get(order_id, session)
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Заказ не найден!"
        )

    update_order = await order_crud.update(
        db_obj=db_order,
        obj_in=order.dict(),
        session=session,
    )
    return update_order
