from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy import desc
from sqlalchemy.orm import Session

from pydantic import BaseModel as PydanticBaseModel

from app.models.base import BaseModel
from app.schemes.filters import Pagination
from app.core.exceptions import NotFoundError, ServerSideError




class BaseRepo:
    def __init__(self, model:BaseModel, session:Callable[..., AbstractContextManager[Session]]) -> None:
        self._session = session
        self._model = model


    def __get_list(self, pag:Pagination) -> list[BaseModel]:
        with self._session() as session:
            return (
                session.query(self._model)
                .order_by(desc(self._model.created_at))
                .offset(pag.page-1 * pag.limit).limit(pag.limit)
            ).all()


    def __get_by_id(self, id:int) -> BaseModel:
        with self._session() as session:
            obj = session.query(self._model).filter(self._model.id==id).first()
            
            if obj is None: raise NotFoundError(f'Not found with id={id}')

            return obj
        

    def __update(self, id:int, schema:PydanticBaseModel, exclude_none:bool = True) -> BaseModel:
        with self._session() as session:
            try:
                query = session.query(self._model).filter(self._model.id==id).update(**schema.model_dump(exclude_none=exclude_none))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            
            return self.__get_by_id(id)


    def __delete(self, id:int) -> None:
        with self._session() as session:
            obj = session.query(self._model).filter(self._model.id==id).first()

            if obj is None:
                raise NotFoundError(f'Not found with id={id}')
            
            try:
                session.delete(obj)
                session.commit()
            except:
                raise ServerSideError("Delete error")
