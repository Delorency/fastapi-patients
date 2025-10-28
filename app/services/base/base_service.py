from pydantic import BaseModel

from app.models.base import BaseModel
from app.repos.base import BaseRepo
from app.schemes.filters import Pagination



class BaseService:
    def __init__(self, repo:BaseRepo) -> None:
        self._repo = repo 

    def get_list(self, pag:Pagination) -> list[BaseModel]:
        return self._repo._get_list(pag)
    
    def get_by_id(self, id:int) -> BaseModel:
        return self._repo._get_by_id(id)
    
    def create(self, schema:BaseModel) -> BaseModel:
        return self._repo._create(schema)
    
    def full_update(self, id:int, schema:BaseModel) -> BaseModel:
        return self._repo._update(id, schema, exclude_none=False)
    
    def partial_update(self, id:int, schema:BaseModel) -> BaseModel:
        return self._repo._update(id, schema, exclude_none=True)
    
    def delete(self, id:int):
        return self._repo._delete(id)