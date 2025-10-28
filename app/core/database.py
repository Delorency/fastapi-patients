from typing import Callable
from contextlib import contextmanager, AbstractContextManager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session



class Database:
    def __init__(self, uri:str) -> None:
        self._engine = create_engine(url=uri, echo=True)
        self._sessionmaker = sessionmaker(bind=self._engine, autoflush=True)
        self._scoped_session = scoped_session(self._sessionmaker)


    @contextmanager 
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._scoped_session()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()