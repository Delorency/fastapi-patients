from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session, selectinload

from .base import BaseRepo

from app.core.exceptions import BadRequestError, NotFoundError, ServerSideError
from app.models import Doctor
from app.schemes.patient_schema import PatientCreateRequest
from .patient2doctor_repo import Patient2DoctorRepo



class DoctorRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]], p2d:Patient2DoctorRepo) -> None:
        super().__init__(Doctor, session)
        self.p2d_repo = p2d


    def _get_by_id_with_many2many(self, id:int) -> Doctor:
        with self._session() as session:
            obj = (
                session.query(self._model)
                .filter(self._model.id==id)
                .options(selectinload(self._model.patients))
                .first()
            )
            
            if obj is None:
                raise NotFoundError(f'Not found with id={id}')

            return obj
        return ServerSideError()


    def _create(self, schema:PatientCreateRequest) -> Doctor:
        data = schema.model_dump()

        patients_list = data.get("patients", [])
        del data["patients"]

        obj = self._model(**data)
        id:int
        with self._session() as session:
            try:
                session.add(obj)
                session.flush()
                session.add_all( self.p2d_repo._patients2doctor_list(obj.id, patients_list) )
                session.commit()

                if hasattr(obj, 'patients'): obj.patients

                return obj
            except Exception as e:
                session.rollback()
                raise BadRequestError()

        return ServerSideError()