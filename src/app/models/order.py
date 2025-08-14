from sqlalchemy import Column, Integer, Text, ForeignKey

from app.core.db import Base


class Order(Base):
    __tablename__ = 'order'
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
