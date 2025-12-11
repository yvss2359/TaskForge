from sqlmodel import Session, select
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from fastapi import HTTPException


def get_tasks_by_project(session: Session, project_id: int, skip=0, limit=50):
    return session.exec(
        select(Task).where(Task.project_id == project_id).offset(skip).limit(limit)
    ).all()


def get_task(session: Session, project_id: int, task_id: int):
    task = session.exec(
        select(Task)
        .where(Task.id == task_id)
        .where(Task.project_id == project_id)
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


def create_task(session: Session, project_id: int, payload: TaskCreate):
    task = Task(
        **payload.dict(),
        project_id=project_id
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update_task(session: Session, project_id: int, task_id: int, payload: TaskUpdate):
    task = get_task(session, project_id, task_id)

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def delete_task(session: Session, project_id: int, task_id: int):
    task = get_task(session, project_id, task_id)
    session.delete(task)
    session.commit()
    return {"ok": True}
