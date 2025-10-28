from datetime import datetime

from typing import Literal
from pydantic import BaseModel, Field

from .base import BaseSchema



class DoctorForPatientSchema(BaseModel, BaseSchema):
    id:int

    class Config:
        from_attributes = True


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


class PatientCreateRequest(BaseModel, BaseSchema):
    gender:Literal["male", "female"]

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    doctors:list[int]

    class Config:
        from_attributes = True



class PatientUpdateRequest(BaseModel, BaseSchema):
    gender:Literal["male", "female"]

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    class Config:
        from_attributes = True


class PatientChangeDoctorsRequest(BaseModel):
    doctor_id:int

    class Config:
        from_attributes = True