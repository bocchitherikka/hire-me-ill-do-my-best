from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Type, Sequence

from app.models import Task
from .models import Task as TaskModel
from .schemas import Task, TaskCreate, TaskUpdate


def get_tasks(
        db:Session
) -> Sequence[Task]:
    stmt = select(TaskModel)
    return db.execute(stmt).scalars().all()


def get_task(
        db:Session,
        task_id: int
) -> Type[TaskModel]:
    return db.get(TaskModel, task_id)


def create_task(
        db: Session,
        task: TaskCreate
) -> Type[TaskModel]:
    db_task = TaskModel(
        name=task.name,
        description=task.description
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(
        db: Session,
        task_id: int,
        task_update: TaskUpdate
) -> Type[TaskModel]:
    db_task = db.get(TaskModel, task_id)
    if not db_task:
        return None
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(
        db: Session,
        task_id: int
) -> Type[TaskModel]:
    db_task = db.get(TaskModel, task_id)
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task
