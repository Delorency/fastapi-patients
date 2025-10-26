from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .base import BaseRepo

from app.core.exceptions import BadRequestError, ServerSideError
from app.models import Doctor
from app.schemes.patient_schema import PatientCreateRequest
from .patient2doctor_repo import Patient2DoctorRepo



class DoctorRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]], p2d:Patient2DoctorRepo) -> None:
        super().__init__(Doctor, session)
        self.p2d_repo = p2d


    def _create(self, schema:PatientCreateRequest) -> Doctor:
        with self._session() as session:
            data = schema.model_dump()

            patients_list = data.get("patients", [])
            del data["patients"]

            obj = self._model(**data)
            try:
                session.add(obj)
                session.commit()
                session.refresh(obj)
                self.p2d_repo._doctors2patient(obj.id, patients_list)
            except Exception as e:
                session.rollback()
                raise BadRequestError(str(e.orig))
            return
        return ServerSideError()