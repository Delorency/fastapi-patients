from typing import List

from enum import Enum as PyEnum

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .base import Base, FioBase, association_table_patient_doctor



class Doctor(Base, FioBase):
    __tablename__= "doctor"
    
    patients:Mapped[List["Patient"]] = relationship(
        secondary=association_table_patient_doctor, back_populates="doctors"
    )