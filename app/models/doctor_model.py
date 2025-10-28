from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, FioBase



class Doctor(BaseModel, FioBase):
    __tablename__= "doctor"
    
    patients:Mapped[list["Patient"]] = relationship(
        secondary="patient2doctor",
        back_populates="doctors",
        order_by="desc(Patient.created_at)"
    )