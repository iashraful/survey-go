from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.core.database import get_db


class DataAccessQueryModelManager:

    @classmethod
    def objects(cls, session: Session):
        return session.query(cls)
