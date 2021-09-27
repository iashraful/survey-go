import os

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import List, Optional, Union


class Settings(BaseSettings):
    JWT_SECRET: str = os.environ.get('JWT_SECRET', 'TEST-JWT-SECRET')
    JWT_ALGORITHM: str = "HS256"

    V1_API_PREFIX = '/api/v1'
    V2_API_PREFIX = '/api/v2'
    V3_API_PREFIX = '/api/v3'

    # 60 minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get('DB_CONN_STRING')

    class Config:
        case_sensitive = True


settings = Settings()
