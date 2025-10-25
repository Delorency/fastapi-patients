from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.models.base import Base


class BaseRepo:
    def __init__(self, model:Base, session:Callable[..., AbstractContextManager[Session]]) -> None:
        self._session = session
        self._model = model