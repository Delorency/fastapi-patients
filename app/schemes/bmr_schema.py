from datetime import datetime
from pydantic import field_validator, BaseModel

from .base import BaseSchema



class PatientForBMRSchema(BaseModel, BaseSchema):
    id:int
    height:int
    weight:int 
    gender:str

    @field_validator('gender', mode='before')
    @classmethod
    def validate_gender(cls, v):
        if hasattr(v, 'value'):
            return v.value
        return v


class BMRSchema(BaseModel):
    id:int
    formula:str
    bmr_value:float
    created_at:datetime

    @field_validator('formula', mode='before')
    @classmethod
    def validate_gender(cls, v):
        if hasattr(v, 'value'):
            return v.value
        return v