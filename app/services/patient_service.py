from app.repos import PatientRepo
from app.schemes.filters import Pagination, FullNameFilter, AgeFilter, GenderFilter
from app.models import Patient

from .base import BaseService



class PatientService(BaseService):
    def __init__(self, repo:PatientRepo) -> None:
        super().__init__(repo)

    def get_list_with_filters(self,
        pag:Pagination, full_name_filter:FullNameFilter, age_filter:AgeFilter, gender_filter:GenderFilter ) -> list[Patient]:
        return self._repo._get_list_with_filters(pag, full_name_filter, age_filter, gender_filter)

    def add_doctor(self, patient_id:int, doctor_id:int) -> None:
        return self._repo._add_doctor_to_patient(patient_id, doctor_id)
    
    def remove_doctor(self, patient_id:int, doctor_id:int) -> None:
        return self._repo._remove_doctor_from_patient(patient_id, doctor_id)