from app.repos import DoctorRepo
from .base import BaseService



class DoctorService(BaseService):
    def __init__(self, repo:DoctorRepo) -> None:
        super().__init__(repo)

    def add_patient(self, doctor_id:int, patient_id:int) -> None:
        return self._repo._add_patient_to_doctor(doctor_id, patient_id)
    
    def remove_patient(self, doctor_id:int, patient_id:int) -> None:
        return self._repo._remove_patient_from_doctor(doctor_id, patient_id)