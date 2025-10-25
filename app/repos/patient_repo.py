from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from .base import BaseRepo

from app.models import Patient
from .patient2doctor_repo import Patient2DoctorRepo



class PatientRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]], p2d:Patient2DoctorRepo) -> None:
        super().__init__(Patient, session)
        self.p2d_repo = p2d