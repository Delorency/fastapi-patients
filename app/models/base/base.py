from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime, func, Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(BigInteger, primary_key=True)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_onupdate=func.now())



class FioBase(DeclarativeBase):
    first_name:Mapped[str] = mapped_column(String(128))
    last_name:Mapped[str] = mapped_column(String(128))
    middle_name:Mapped[str] = mapped_column(String(128))



# association_table_patient_doctor = Table(
#     "association_table",
#     Base.metadata,
#     Column("patient_id", ForeignKey("patient.id"), primary_key=True),
#     Column("doctor_id", ForeignKey("doctor.id"), primary_key=True),
# )