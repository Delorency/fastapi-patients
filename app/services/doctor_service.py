from app.repos import DoctorRepo
from .base import BaseService



class DoctorService(BaseService):
    def __init__(self, repo:DoctorRepo) -> None:
        super().__init__(repo)