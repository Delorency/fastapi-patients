from typing import List
from pydantic import BaseModel

from app.models.base import Base
from app.repos.base import BaseRepo
from app.schemes.filters import Pagination



class BaseService:
    def __init__(self, repo:BaseRepo) -> None:
        self,_repo = repo 

    def get_list(self, pag:Pagination) -> List[Base]:
        return self._repo._get_list(pag)
    
    def get_by_id(self, id:int) -> Base:
        return self._repo._get_by_id(id)
    
    def create(self, schema:BaseModel) -> Base:
        return self._repo._create(schema)
    
    def delete(self, id:int):
        return self._repo._delete(id)