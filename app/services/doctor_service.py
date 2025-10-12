from app.repos.base import BaseRepo
from .base import BaseService



class DoctorService(BaseService):
    def __init__(self, repo:BaseRepo) -> None:
        super().__init__(repo)