from datetime import date

from enum import Enum as PyEnum

from sqlalchemy import SmallInteger, func, Date, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, FioBase
from .patient2doctor import Patient2Doctor



class PatientGender(PyEnum):
    male = "male"
    female = "female"


class Patient(BaseModel, FioBase):
    __tablename__= "patient"
    birthday:Mapped[date] = mapped_column(Date)
    
    gender:Mapped[PyEnum] = mapped_column(Enum(PatientGender, name="patient_gender_enum"))

    height:Mapped[int] = mapped_column(SmallInteger)
    weight:Mapped[int] = mapped_column(SmallInteger)

    doctors:Mapped[list["Doctor"]] = relationship(
        secondary=Patient2Doctor,
        back_populates="patients",
        order_by="desc(Doctor.created_at)"
    )

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', 'middle_name'),
    )