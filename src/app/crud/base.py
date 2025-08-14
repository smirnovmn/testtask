from typing import Any, Dict, Optional, Sequence, Type
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class BaseCRUD:
    """базовый CRUD."""

    def __init__(self, model: Type[Any]) -> None:
        self.model = model

    async def get(self, obj_id: int, session: AsyncSession) -> Optional[Any]:
        result = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalars().first()

    async def get_multi(
        self,
        session: AsyncSession,
        *filters: Any,
    ) -> Sequence[Any]:
        stmt = select(self.model).where(*filters) if filters else select(self.model)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def create(
        self,
        obj_in: Dict[str, Any],
        session: AsyncSession,
        user: Optional[User] = None,
    ) -> Any:
        """Метод создает и возвращает новый объект модели."""
        if user:
            obj_in['user_id'] = user.id
        db_obj = self.model(**obj_in)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self, db_obj: Any, obj_in: Dict[str, Any], session: AsyncSession
    ) -> Any:
        for field, value in obj_in.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(self, db_obj: Any, session: AsyncSession) -> None:
        await session.delete(db_obj)
        await session.commit()
