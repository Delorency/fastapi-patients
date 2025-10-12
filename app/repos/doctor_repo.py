from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from .base import BaseRepo

from app.models import Doctor



class DoctorRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]]) -> None:
        super().__init__(Doctor, session)