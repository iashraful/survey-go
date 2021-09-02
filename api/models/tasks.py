from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from api.core.database import ModelBase


class TaskModel(ModelBase):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(Integer)
    execution_time = Column(DateTime)
