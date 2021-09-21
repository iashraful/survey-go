from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.core.auth import authenticate, create_access_token, get_current_user
from api.core.database import get_db
from api.core.security import get_password_hash
from api.survey.models.user import User
from api.survey.schemas.v1.user import UserCreateSchema, UserListSchema

router = APIRouter()


@router.post(path='/login/', status_code=200)
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_instance = authenticate(email=form_data.username, password=form_data.password, db=db)
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
def get_users(db: Session = Depends(get_db), c_user: User = Depends(get_current_user)):
    users = User.objects(db).all()
    return users


@router.post(path='/users/', response_model=UserListSchema, status_code=201)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    instance = User.objects(db).filter_by(email=user.email).first()
    if instance:
        raise HTTPException(
            status_code=400,
            detail='User already exist on the system.'
        )
    _password_hash = get_password_hash(password=user.password)
    instance = User(name=user.name, email=user.email, password=_password_hash)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


@router.get(path='/me/', response_model=UserListSchema, status_code=200)
def get_login_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user
