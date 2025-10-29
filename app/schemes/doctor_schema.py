from datetime import datetime

from typing import Optional, Literal
from pydantic import BaseModel, Field, field_validator

from .base import BaseSchema



class PatientForDoctorSchema(BaseModel, BaseSchema):
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


class DoctorSchema(BaseModel, BaseSchema):
    id:int

    patients:list[PatientForDoctorSchema]

    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True


class DoctorGetListSchema(BaseModel, BaseSchema):
    id:int

    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True


class DoctorCreateRequest(BaseSchema, BaseModel):

    patients:list[int]
    
    class Config:
        from_attributes = True



class DoctorUpdateRequest(BaseModel):
    last_name:Optional[str] = None
    first_name:Optional[str] = None
    middle_name:Optional[str] = None

    class Config:
        from_attributes = True