from pydantic import BaseModel

from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from .base import BaseRepo

from app.models import Doctor
from .patient2doctor_repo import Patient2DoctorRepo



class DoctorRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]], p2d:Patient2DoctorRepo) -> None:
        super().__init__(Doctor, session)
        self.p2d_repo = p2d