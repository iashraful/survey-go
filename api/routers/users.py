from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.core.database import get_db
from api.models.user import User
from api.schemas.user import UserCreateSchema

router = APIRouter()


@router.post(path='/users/', response_model=UserCreateSchema, status_code=201)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    # TODO: Do a password hash and save to db
    instance = User(name=user.name, email=user.email)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
