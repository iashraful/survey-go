from sqlalchemy.orm import Session
from starlette.requests import Request


class DataAccessQueryModelManager:

    @classmethod
    def objects(cls, session: Session, request: Request = None):
        return session.query(cls)
