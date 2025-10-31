from datetime import datetime
from pydantic import field_validator

from .base import BaseSchema
from .patient_schema import PatientGetListSchema



class MBRCreateRequest(BaseSchema):
    patient_id:int



class MBRSchema(BaseSchema):
    id:int
    patient:list[PatientGetListSchema]
    formula:str
    created_at:datetime

    @field_validator('formula', mode='before')
    @classmethod
    def validate_gender(cls, v):
        if hasattr(v, 'value'):
            return v.value
        return v