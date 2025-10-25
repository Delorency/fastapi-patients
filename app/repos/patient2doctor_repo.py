from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.base import BaseRepo
from app.models import Patient2Doctor
from app.core.exceptions import BadRequestError, ServerSideError



class Patient2DoctorRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]]) -> None:
        super().__init__(Patient2Doctor, session)

    def __patients2doctor(self, doctor_id:int, patients:list[int]):
        list_data:list[Patient2Doctor] = [ Patient2Doctor(doctor_id=doctor_id, patient_id=id) for id in patients ] 
        with self._session() as session:
            try:
                session.add_all(list_data)
                session.commit()
            except IntegrityError as e:
                raise BadRequestError(str(e.orig))
            return 
        return ServerSideError
    
    def __doctors2patient(self, patient_id:int, doctors:list[int]):
        list_data:list[Patient2Doctor] = [ Patient2Doctor(patient_id=patient_id, doctor_id=id, ) for id in doctors ] 
        with self._session() as session:
            try:
                session.add_all(list_data)
                session.commit()
            except IntegrityError as e:
                raise BadRequestError(str(e.orig))
            return 
        return ServerSideError