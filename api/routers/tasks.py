from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.enums.task_enums import TaskStatusEnum
from api.core.database import get_db
from api.models.tasks import TaskModel
from api.schemas.tasks import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from fastapi import APIRouter

router = APIRouter()

@router.get('/tasks/', response_model=List[TaskSchema])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).order_by(TaskModel.execution_time.desc()).all()
    return tasks


@router.post(path='/tasks/', response_model=TaskSchema, status_code=201)
def create_task(task: TaskCreateSchema, db: Session = Depends(get_db)):
    task_instance = TaskModel(
        title=task.title, description=task.description,
        execution_time=task.execution_time, status=TaskStatusEnum.Pending.value
    )
    db.add(task_instance)
    db.commit()
    db.refresh(task_instance)
    return task_instance


@router.get(path='/tasks/{id}/', response_model=TaskSchema)
def get_task(id, db: Session = Depends(get_db)):
    task_instance = db.query(TaskModel).get(ident=id)
    return task_instance


@router.put(path='/tasks/{id}/', response_model=TaskSchema)
def update_task(task:TaskUpdateSchema, id, db: Session = Depends(get_db)):
    task_instance = db.query(TaskModel).get(ident=id)
    task_instance.title = task.title
    task_instance.description = task.description
    task_instance.execution_time = task.execution_time
    task_instance.status = task.status
    db.commit()
    return task_instance
