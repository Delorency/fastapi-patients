from enum import Enum as PyEnum

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel



class MbrEnum(PyEnum):
    mif_sanj = 'Mifflin-St Jeor equation'
    har_ben = 'Harris-Benedict equation'


class MBR(BaseModel):
    __tablename__='mbr'

    formula:Mapped[PyEnum] = mapped_column(Enum(MbrEnum, name='mbr_enum'))
    patient:Mapped[int] = mapped_column(ForeignKey('patient.id', ondelete='CASCADE'))