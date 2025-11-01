from enum import Enum as PyEnum

from sqlalchemy import ForeignKey, Enum, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel



class BMREnum(PyEnum):
    mif_sanj = 'mifflin-at jeor equation'
    har_ben = 'harris-benedict equation'


class BMR(BaseModel):
    __tablename__='bmr'

    formula:Mapped[PyEnum] = mapped_column(Enum(BMREnum, name='bmr_enum'))
    bmr_value:Mapped[float] = mapped_column(Numeric(6,2))
    patient_id:Mapped[int] = mapped_column(ForeignKey('patient.id', ondelete='CASCADE'))
    patient:Mapped["Patient"] = relationship()