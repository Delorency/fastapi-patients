from typing import Callable
from contextlib import AbstractContextManager

from sqlalchemy.orm import Session

from app.models import MBR
from .base import BaseRepo



class MBRRepo(BaseRepo):
    def __init__(self, session:Callable[..., AbstractContextManager[Session]]) -> None:
        super().__init__(MBR, session)