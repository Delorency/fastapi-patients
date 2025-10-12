from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session, selectinload

from app.models.base import Base
from app.schemes.filters import Pagination


class BaseRepo:
    def __init__(self, model:Base, session:Callable[..., AbstractContextManager[Session]]) -> None:
        self._session = session
        self._model = model