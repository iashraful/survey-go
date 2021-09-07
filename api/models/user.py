from typing import Any

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Session
from starlette.authentication import UnauthenticatedUser
from starlette.requests import Request

from api.core.access_control import DataAccessQueryModelManager
from api.core.model_base import ModelBase


class User(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'users'
