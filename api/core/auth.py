import binascii
from datetime import datetime, timedelta
from typing import MutableMapping, Union, List, Optional, Any

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from jose import jwt, JWTError
from starlette.authentication import AuthenticationBackend, AuthenticationError

from api.core.config import settings
from api.core.database import get_db, LocalSession
from api.core.security import verify_password
from api.models import User

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.V1_API_PREFIX}/login/')


# Declaring a Token schema here because it's too much related here only
class TokenData(BaseModel):
    username: Optional[str] = None


class BearerTokenAuthBackend(AuthenticationBackend):
    """
    This is a custom auth backend class which will allow you to authenticate your request and return auth and user as
    a tuple
    """
    async def authenticate(self, request):
        # This function is inherited from the base class and called by some other class
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, token = auth.split()
            if scheme.lower() != 'bearer':
                return
            decoded = jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithms=[settings.JWT_ALGORITHM],
                options={"verify_aud": False},
            )
        except (ValueError, UnicodeDecodeError, JWTError) as exc:
            raise AuthenticationError('Invalid JWT Token.')

        username: str = decoded.get("sub")
        token_data = TokenData(username=username)
        # This is little hack rather making a generator function for get_db
        db = LocalSession()
        user = User.objects(db).filter(User.id == token_data.username).first()
        # We must close the connection
        db.close()
        if user is None:
            raise AuthenticationError('Invalid JWT Token.')
        return auth, user


def authenticate(*, email: str, password: str, db: Session) -> Optional[User]:
    user = User.objects(db).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_access_token(*, sub: str) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
    )


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> Any:
    try:
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = User.objects(db).filter(User.id == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user


def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
