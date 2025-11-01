from typing import Callable
from contextlib import AbstractContextManager

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.core.exceptions import BadRequestError, ServerSideError
from app.models import BMR

from app.schemes.filters import Pagination
from .base import BaseRepo



class BMRRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]]) -> None:
        super().__init__(BMR, session)

    def _get_bmr_list(self, patient_id:int, pag:Pagination) -> list[BMR]:
        with self._session() as session:
            return (
                session.query(self._model)
                .filter(self._model.patient_id==patient_id)
                .order_by(desc(self._model.created_at))
                .offset((pag.page-1) * pag.limit).limit(pag.limit)
                .all()
            )
        raise ServerSideError()

    def _create(self, patient_id:int, formula:str, bmr_value:float) -> BMR:
        with self._session() as session:
            obj = self._model(patient_id=patient_id, formula=formula, bmr_value=bmr_value)
            try:
                session.add(obj)
                session.commit()
                session.refresh(obj)
            except:
                raise BadRequestError()
            
            return obj
        raise ServerSideError()