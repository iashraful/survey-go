from pydantic import BaseModel, validator


class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str

    class Config:
        orm_mode = True

    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
