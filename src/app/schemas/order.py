from pydantic import BaseModel


class OrderBase(BaseModel):
    name: str
    description: str | None = None


class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
