from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead

router = APIRouter()

@router.get("/", response_model=list[TaskRead])
def list_tasks(skip: int = 0, limit: int = 50, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).offset(skip).limit(limit)).all()
    return tasks

@router.post("/", response_model=TaskRead)
def create_task(payload: TaskCreate, session: Session = Depends(get_session)):
    task = Task(**payload.dict(), owner_id=1)  # temporaire: owner_id=1
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
