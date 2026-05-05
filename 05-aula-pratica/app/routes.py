from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import TaskCreate, TaskResponse, TaskUpdate
from app import db
from app.models import Task

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, session: Session = Depends(db.get_session)):
    task = Task(
        title=payload.title,
        status=(
            payload.status.value if hasattr(payload.status, "value") else payload.status
        ),
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.get("/tasks", response_model=List[TaskResponse])
def list_tasks(session: Session = Depends(db.get_session)):
    tasks = session.query(Task).order_by(Task.created_at.desc()).all()
    return tasks


@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int, payload: TaskUpdate, session: Session = Depends(db.get_session)
):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não foi encontrada")

    if payload.title is not None:
        task.title = payload.title
    if payload.status is not None:
        task.status = (
            payload.status.value if hasattr(payload.status, "value") else payload.status
        )

    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(db.get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não foi encontrada")
    session.delete(task)
    session.commit()
    return None
