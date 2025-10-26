from datetime import datetime

from typing import Literal
from pydantic import BaseModel, Field

from .base import BaseSchema


class DoctorForPatientSchema(BaseSchema, BaseModel):
    id:int


class PatientSchema(BaseSchema, BaseModel):
    id:int

    gender:Literal["male", "female"]

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    doctors:list[DoctorForPatientSchema]

    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True


class PatientCreateRequest(BaseSchema, BaseModel):
    gender:Literal["male", "female"]

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    doctors:list[int]

    class Config:
        from_attributes = True