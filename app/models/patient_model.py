from typing import List
from datetime import date

from enum import Enum as PyEnum

from sqlalchemy import SmallInteger, func, Date, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, FioBase, association_table_patient_doctor



class PatientGender(PyEnum):
    male = "male"
    female = "female"


class Patient(Base, FioBase):
    __tablename__= "patient"
    birthday:Mapped[date] = mapped_column(Date)
    
    gender:Mapped[PyEnum] = mapped_column(Enum(PatientGender, name="patient_gender_enum"))

    height:Mapped[int] = mapped_column(SmallInteger)
    weight:Mapped[int] = mapped_column(SmallInteger)

    doctors:Mapped[List["Doctor"]] = relationship(
        secondary=association_table_patient_doctor,
        back_populates="patients",
        order_by="desc(Doctor.created_at)"
    )

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', 'middle_name'),
    )