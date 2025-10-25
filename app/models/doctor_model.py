from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel, FioBase
from .patient2doctor import Patient2Doctor



class Doctor(BaseModel, FioBase):
    __tablename__= "doctor"
    
    patients:Mapped[list["Patient"]] = relationship(
        secondary=Patient2Doctor,
        back_populates="doctors",
        order_by="desc(Patient.created_at)"
    )