from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Status(str, Enum):
    pending = "pending"  # pendente
    doing = "doing"  # em progresso
    done = "done"  # feito


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    status: Optional[Status] = Status.pending


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    status: Optional[Status]


class TaskResponse(BaseModel):
    id: int
    title: str
    status: Status
    created_at: datetime

    class Config:
        orm_mode = True
