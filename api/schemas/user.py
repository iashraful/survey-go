import re
from pydantic import BaseModel, validator


class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str

    class Config:
        orm_mode = True

    @validator('email')
    def email_validation(cls, v, values, **kwargs):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, v):
            raise ValueError('Email should be a valid email.')
        return v

    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v


class UserListSchema(BaseModel):
    id: int
    name: str
    email: str
    email_verified: bool
    is_active: bool

    class Config:
        orm_mode = True


class UserBasicSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

    @validator('email')
    def email_validation(cls, v, values, **kwargs):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, v):
            raise ValueError('Email should be a valid email.')
        return v


class LoginResponseSchema(BaseModel):
    email: str
    token: str

    class Config:
        orm_mode = True
