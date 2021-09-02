from pydantic import BaseModel
from datetime import datetime


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    execution_time: datetime
    status: int

    class Config:
        orm_mode = True

class TaskCreateSchema(BaseModel):
    title: str
    description: str
    execution_time: datetime

    class Config:
        orm_mode = True

class TaskUpdateSchema(BaseModel):
    title: str
    description: str
    execution_time: datetime
    status: int

    class Config:
        orm_mode = True
