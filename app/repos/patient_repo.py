from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from .base import BaseRepo

from app.core.exceptions import BadRequestError, ServerSideError
from app.models import Patient
from app.schemes.patient_schema import PatientCreateRequest
from .patient2doctor_repo import Patient2DoctorRepo



class PatientRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]], p2d:Patient2DoctorRepo) -> None:
        super().__init__(Patient, session)
        self.p2d_repo = p2d


    def _create(self, schema:PatientCreateRequest) -> Patient:
        with self._session() as session:
            data = schema.model_dump()

            doctors_list = data.get("doctors", [])
            del data["doctors"]

            obj = self._model(**data)
            try:
                session.add(obj)
                session.commit()
                session.refresh(obj)
                self.p2d_repo._add_doctors2patient(obj.id, doctors_list)
                session.refresh(obj)
            except Exception as e:
                session.rollback()
                raise BadRequestError(str(e.orig))
            return obj
        return ServerSideError()
    

    def _add_doctor_to_patient(self, patient_id:int, doctor_id:int) -> None:
        return self.p2d_repo._create_doctor_patient_pair(patient_id, doctor_id)

    def _remove_doctor_from_patient(self, patient_id:int, doctor_id:int) -> None:
        return self.p2d_repo._delete_doctor_patient_pair(patient_id, doctor_id)