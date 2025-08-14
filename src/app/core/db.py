# from sqlalchemy import Column, Integer
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

# from app.core.config import settings


# class PreBase:

#     @declared_attr
#     def __tablename__(cls):
#         return cls.__name__.lower()

#     id = Column(Integer, primary_key=True)


# Base = declarative_base(cls=PreBase)

# engine = create_async_engine(settings.database_url)

# AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


# async def get_async_session():
#     async with AsyncSessionLocal() as async_session:
#         yield async_session


from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)


Base = declarative_base(cls=PreBase)

# Для PostgreSQL обязательно postgresql+asyncpg://...
engine = create_async_engine(
    settings.database_url,
    echo=True,  # Лог запросов в консоль (выключи на проде)
    future=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
