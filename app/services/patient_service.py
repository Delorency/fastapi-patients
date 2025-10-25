from app.repos import PatientRepo
from .base import BaseService



class PatientService(BaseService):
    def __init__(self, repo:PatientRepo) -> None:
        super().__init__(repo)