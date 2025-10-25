from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base



class Patient2Doctor(Base):
    __tablename__ = "patient2doctor"
    patient_id: Mapped[int] = mapped_column(ForeignKey('patient.id', ondelete="CASCADE"), primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctor.id', ondelete="CASCADE"), primary_key=True)

    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())