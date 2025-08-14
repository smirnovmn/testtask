from fastapi_users import schemas
from pydantic import Field


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    age: int = Field(..., gt=0)


class UserUpdate(schemas.BaseUserUpdate):
    age: int | None = Field(None, gt=0)

