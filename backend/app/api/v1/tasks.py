from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.task import TaskRead, TaskCreate, TaskUpdate
from app.crud.crud_task import (
    get_tasks_by_project,
    get_task,
    create_task,
    update_task,
    delete_task
)

router = APIRouter()


# --- GET /projects/{project_id}/tasks ---
@router.get("/projects/{project_id}/tasks", response_model=list[TaskRead])
def list_tasks_route(
    project_id: int,
    skip: int = 0,
    limit: int = 50,
    session: Session = Depends(get_session)
):
    return get_tasks_by_project(session, project_id, skip, limit)


# --- GET /projects/{project_id}/tasks/{task_id} ---
@router.get("/projects/{project_id}/tasks/{task_id}", response_model=TaskRead)
def read_task_route(
    project_id: int,
    task_id: int,
    session: Session = Depends(get_session)
):
    return get_task(session, project_id, task_id)


# --- POST /projects/{project_id}/tasks ---
@router.post("/projects/{project_id}/tasks", response_model=TaskRead)
def create_new_task_route(
    project_id: int,
    payload: TaskCreate,
    session: Session = Depends(get_session)
):
    return create_task(session, project_id, payload)


# --- PUT /projects/{project_id}/tasks/{task_id} ---
@router.put("/projects/{project_id}/tasks/{task_id}", response_model=TaskRead)
def edit_task_route(
    project_id: int,
    task_id: int,
    payload: TaskUpdate,
    session: Session = Depends(get_session)
):
    return update_task(session, project_id, task_id, payload)


# --- DELETE /projects/{project_id}/tasks/{task_id} ---
@router.delete("/projects/{project_id}/tasks/{task_id}")
def remove_task_route(
    project_id: int,
    task_id: int,
    session: Session = Depends(get_session)
    ):
    
    return delete_task(session, project_id, task_id)
