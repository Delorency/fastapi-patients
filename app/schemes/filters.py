from typing import Optional, Literal
from pydantic import BaseModel, field_validator, Field

from app.core.config import configs


class Pagination(BaseModel):
    page:int = configs.apicfg.page
    limit:int = configs.apicfg.limit

    @field_validator('page')
    def validate_page(cls, value):
        if value <= 0:
            return configs.apicfg.page
        return value
        
    @field_validator('limit')
    def validate_limit(cls, value):
        if value < 0:
            return configs.apicfg.limit
        return value

class FullNameFilter(BaseModel):
    full_name:Optional[str] = Field(None)

class AgeFilter(BaseModel):
    start_age:Optional[int] = Field(None, gt=0)
    end_age:Optional[int] = Field(None, gt=0)

class GenderFilter(BaseModel):
    gender:Optional[Literal["male", "female"]] = None