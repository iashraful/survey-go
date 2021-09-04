from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

from api.core.model_base import ModelBase


class TaskModel(ModelBase):
    # Will be removed later
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(Integer)
    execution_time = Column(DateTime)

