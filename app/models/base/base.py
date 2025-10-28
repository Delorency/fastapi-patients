from typing import Optional
from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime, func, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



class Base(DeclarativeBase): pass


class BaseModel(Base):
    __abstract__ = True
    id:Mapped[int] = mapped_column(BigInteger, primary_key=True)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), default=func.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_onupdate=func.now(), default=func.now())


class FioBase(Base):
    __abstract__ = True
    first_name:Mapped[str] = mapped_column(String(128))
    last_name:Mapped[str] = mapped_column(String(128))
    middle_name: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', 'middle_name'),
    )