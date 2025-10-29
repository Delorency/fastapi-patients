from datetime import datetime, date

from typing import Literal, Optional
from pydantic import BaseModel, Field, field_validator

from .base import BaseSchema



class DoctorForPatientSchema(BaseModel, BaseSchema):
    id:int

    class Config:
        from_attributes = True


class PatientSchema(BaseModel, BaseSchema):
    id:int

    gender:Literal["male", "female"]

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    doctors:list[DoctorForPatientSchema]

    created_at:datetime
    updated_at:datetime


    @field_validator('gender', mode='before')
    @classmethod
    def validate_gender(cls, v):
        if hasattr(v, 'value'):
            return v.value
        return v

    class Config:
        from_attributes = True


class PatientGetListSchema(BaseModel, BaseSchema):
    id:int

    gender:Literal["male", "female"]

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    created_at:datetime
    updated_at:datetime


    @field_validator('gender', mode='before')
    @classmethod
    def validate_gender(cls, v):
        if hasattr(v, 'value'):
            return v.value
        return v

    class Config:
        from_attributes = True


class PatientCreateRequest(BaseSchema, BaseModel):
    gender:Literal["male", "female"]

    birthday:date

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    doctors:list[int]

    class Config:
        from_attributes = True



class PatientUpdateRequest(BaseModel):
    last_name:Optional[str] = None
    first_name:Optional[str] = None
    middle_name:Optional[str] = None
    gender:Optional[Literal["male", "female"]] = None

    height:Optional[int] = Field(None, gt=0)
    weight:Optional[int] = Field(None, gt=0)

    class Config:
        from_attributes = True


class PatientChangeDoctorsRequest(BaseModel):
    doctor_id:int

    class Config:
        from_attributes = True