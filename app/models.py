from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Column, Integer, String

from .database import Base


class TaskStatus(Enum):
    created = "created"
    in_progress = "in_progress"
    completed = "completed"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.created)
