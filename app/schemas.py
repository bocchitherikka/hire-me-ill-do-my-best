from enum import Enum
from pydantic import BaseModel
from typing import Optional


class TaskStatus(str, Enum):
    created = "created"
    in_progress = "in_progress"
    completed = "completed"


class Task(BaseModel):
    id: int
    name: str
    description: str
    status: TaskStatus = TaskStatus.created

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    name: str
    description: str


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
