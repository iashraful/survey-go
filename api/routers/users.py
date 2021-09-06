from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.core.auth import authenticate, create_access_token
from api.core.database import get_db
from api.core.security import get_password_hash, verify_password
from api.models.user import User
from api.schemas.user import UserCreateSchema, LoginSchema, LoginResponseSchema, UserListSchema

router = APIRouter()


@router.post(path='/login/', status_code=200)
def user_login(user: LoginSchema, db: Session = Depends(get_db)):
    user_instance = authenticate(email=user.email, password=user.password, db=db)
    if user_instance:
        return {
            'access_token': create_access_token(sub=str(user_instance.id)),
            'token_type': 'bearer',
        }
    raise HTTPException(
        status_code=400,
        detail='Login credentials are wrong.'
    )


@router.get(path='/users/', response_model=List[UserListSchema], status_code=200)
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post(path='/users/', response_model=UserListSchema, status_code=201)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    instance = db.query(User).filter_by(email=user.email).first()
    if instance:
        _password_hash = get_password_hash(password=user.password)
        raise HTTPException(
            status_code=400,
            detail='User already exist on the system.'
        )
    instance = User(name=user.name, email=user.email, password=_password_hash)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
