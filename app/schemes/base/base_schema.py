from typing import Optional
from pydantic import BaseModel



class BaseSchema:
    last_name:str
    first_name:str
    middle_name:Optional[str] 