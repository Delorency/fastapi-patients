from datetime import date
from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy import func, desc
from sqlalchemy.orm import Session, selectinload

from .base import BaseRepo

from app.core.exceptions import BadRequestError, NotFoundError, ServerSideError
from app.models import Patient
from app.schemes.patient_schema import PatientCreateRequest
from .patient2doctor_repo import Patient2DoctorRepo
from app.schemes.filters import Pagination, FullNameFilter, AgeFilter, GenderFilter



class PatientRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]], p2d:Patient2DoctorRepo) -> None:
        super().__init__(Patient, session)
        self.p2d_repo = p2d

    def _get_list_with_filters(self, pag:Pagination, full_name_filter:FullNameFilter,
        age_filter:AgeFilter, gender_filter:GenderFilter ) -> list[Patient]:
        with self._session() as session:
            query = session.query(self._model)
            if gender_filter.gender is not None: query = query.filter(self._model.gender==gender_filter.gender)

            today = date.today()
            if age_filter.end_age is not None:
                max_birthday = date(today.year-age_filter.end_age, today.month, today.day)
                query = query.filter(self._model.birthday>=max_birthday)
            
            if age_filter.start_age is not None:
                min_birthday = date(today.year-age_filter.start_age, today.month, today.day)
                query = query.filter(self._model.birthday<=min_birthday)

            return query.order_by(desc(self._model.created_at)).offset((pag.page-1)*pag.limit).limit(pag.limit).all()
        return ServerSideError()


    def _get_by_id_with_many2many(self, id:int) -> Patient:
        with self._session() as session:
            obj = (
                session.query(self._model)
                .filter(self._model.id==id)
                .options(selectinload(self._model.doctors))
                .first()
            )
            
            if obj is None:
                raise NotFoundError(f'Not found with id={id}')

            return obj
        return ServerSideError()


    def _create(self, schema:PatientCreateRequest) -> Patient:
        data = schema.model_dump()
        doctors_list = data.get("doctors")
        del data["doctors"]

        obj = self._model(**data)
        with self._session() as session:
            if session.query(self._model).filter(
                self._model.first_name==data["first_name"],
                self._model.middle_name==data["middle_name"],
                self._model.last_name==data["last_name"]
            ).first():
                raise BadRequestError("Already exist")
            try:
                session.add(obj)
                session.flush()
                session.add_all( self.p2d_repo._doctors2patient_list(obj.id, doctors_list) )
                session.commit()

                if hasattr(obj, 'doctors'): obj.doctors

                return obj
            except Exception as e:
                session.rollback()
                raise BadRequestError()
            
        return ServerSideError()
    

    def _add_doctor_to_patient(self, patient_id:int, doctor_id:int) -> None:
        return self.p2d_repo._create_patient_doctor_pair(patient_id, doctor_id)

    def _remove_doctor_from_patient(self, patient_id:int, doctor_id:int) -> None:
        return self.p2d_repo._delete_patient_doctor_pair(patient_id, doctor_id)