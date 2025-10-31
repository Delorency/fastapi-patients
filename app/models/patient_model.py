from datetime import date

from enum import Enum as PyEnum

from sqlalchemy import SmallInteger, func, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, FioBase



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
        secondary="patient2doctor",
        back_populates="patients",
        order_by="desc(Doctor.created_at)"
    )
    mbrs:Mapped[list["MBR"]] = relationship(
        back_populates='patient',
        order_by="desc(MBR.created_at)",
        cascade="all",   
    )