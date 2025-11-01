from datetime import date
from app.repos import PatientRepo
from app.schemes.filters import Pagination, FullNameFilter, AgeFilter, GenderFilter
from app.models import Patient, BMR
from app.models.bmr_model import BMREnum
from app.utils import *

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
    
    def get_bmr_list(self, id:int, pag:Pagination) -> list[BMR]:
        return self._repo._get_bmr_list(id, pag)
    
    def create_bmr(self, patient_id:int, first:bool) -> BMR:
        obj = self._repo._get_by_id(patient_id)
        today = date.today()
        year = today.year - obj.birthday.year

        if obj.birthday.month > today.month or \
            (obj.birthday.month == today.month and  obj.birthday.day > today.day): year-=1
        height = obj.height
        weight = obj.weight

        bmr_value:float
        formula:str 
        if first: bmr_value, formula = generate_bmr_mif_sanj(height, weight, year, obj.gender=='male'), BMREnum.mif_sanj
        else: bmr_value, formula = generate_bmr_har_ben(height, weight, year, obj.gender=='male'), BMREnum.har_ben

        return self._repo._create_bmr(patient_id, formula, bmr_value)