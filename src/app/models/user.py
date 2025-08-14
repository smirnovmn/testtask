from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer
from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    age = Column(Integer, nullable=False)
    __table_args__ = {"extend_existing": True}
