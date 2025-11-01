from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.repos.base import BaseRepo
from app.models import Patient2Doctor
from app.core.exceptions import DuplicatedError, ServerSideError, NotFoundError



class Patient2DoctorRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]]) -> None:
        super().__init__(Patient2Doctor, session)


    def _patients2doctor_list(self, doctor_id:int, patients:list[int]) -> list[Patient2Doctor]:
        return [ self._model(doctor_id=doctor_id, patient_id=id) for id in patients ] 

    def _doctors2patient_list(self, patient_id:int, doctors:list[int]) -> list[Patient2Doctor]:
        return [ self._model(patient_id=patient_id, doctor_id=id) for id in doctors ] 
    

    def _create_patient_doctor_pair(self, patient_id:int, doctor_id:int) -> None:
        with self._session() as session:
            obj = self._model(patient_id=patient_id, doctor_id=doctor_id)
            try:
                session.add(obj)
                session.commit()
            except:
                raise DuplicatedError("Not found or already exist")
            return
        
        return ServerSideError()
    

    def _delete_patient_doctor_pair(self, patient_id:int, doctor_id:int) -> None:
        with self._session() as session:
            obj = session.query(self._model).filter(self._model.patient_id==patient_id, self._model.doctor_id==doctor_id).first()

            if obj is None:
                raise NotFoundError(f'Not found pair with id {patient_id} - {doctor_id}')
            
            try:
                session.delete(obj)
                session.commit()
            except:
                raise ServerSideError("Delete error")
            return
        
        return ServerSideError()