from datetime import datetime

from typing import Optional, Literal
from pydantic import BaseModel, Field



class DoctorForPatientSchema(BaseModel):
    id:int
    last_name:str
    first_name:str
    middle_name:Optional[str]



class PatientSchema(BaseModel):
    id:int
    last_name:str
    first_name:str
    middle_name:Optional[str]

    gender:Literal["male", "female"]

    height:int = Field(..., gt=0)
    weight:int = Field(..., gt=0)

    doctors:list[DoctorForPatientSchema]

    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True
