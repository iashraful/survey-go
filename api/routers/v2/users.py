from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.core.auth import authenticate, create_access_token
from api.core.database import get_db
from api.schemas.v2.user import UserLoginSchema

router = APIRouter()


@router.post(path='/login/', status_code=200)
def user_login(data: UserLoginSchema, db: Session = Depends(get_db)):
    user_instance = authenticate(email=data.username, password=data.password, db=db)
    if user_instance:
        return {
            'access_token': create_access_token(sub=str(user_instance.id)),
            'token_type': 'bearer',
        }
    raise HTTPException(
        status_code=400,
        detail='Login credentials are wrong.'
    )
