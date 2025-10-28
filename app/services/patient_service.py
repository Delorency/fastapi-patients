from app.repos import PatientRepo
from app.schemes.patient_schema import PatientChangeDoctorsRequest

from .base import BaseService



class PatientService(BaseService):
    def __init__(self, repo:PatientRepo) -> None:
        super().__init__(repo)

    def add_doctor(self, patient_id:int, doctor_id:int) -> None:
        return self._repo._add_doctor_to_patient(patient_id, doctor_id)
    
    def remove_doctor(self, patient_id:int, doctor_id:int) -> None:
        return self._repo._remove_doctor_from_patient(patient_id, doctor_id)