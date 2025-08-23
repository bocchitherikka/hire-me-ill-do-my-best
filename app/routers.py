from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .crud import delete_task, get_task, get_tasks, create_task, update_task
from .database import get_db
from .schemas import Task, TaskCreate, TaskUpdate

router = APIRouter()


@router.get("/", response_model=list[Task])
def get_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.post("/", response_model=Task)
def post_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    db_task = update_task(db, task_id, task_update)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
