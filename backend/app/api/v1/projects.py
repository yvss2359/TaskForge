from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session

from app.schemas.project import ProjectRead, ProjectCreate, ProjectUpdate
from app.crud.crud_project import (
    get_projects,
    get_project,
    create_project,
    update_project,
    delete_project
)

router = APIRouter()

# --- GET /projects ---
@router.get("/", response_model=list[ProjectRead])
def list_projects_route(
    skip: int = 0,
    limit: int = 50,
    session: Session = Depends(get_session)
):
    return get_projects(session, skip, limit)


# --- GET /projects/{project_id} ---
@router.get("/{project_id}", response_model=ProjectRead)
def read_project_route(
    project_id: int,
    session: Session = Depends(get_session)
):
    return get_project(session, project_id)


# --- POST /projects ---
@router.post("/", response_model=ProjectRead)
def create_new_project_route(
    payload: ProjectCreate,
    session: Session = Depends(get_session),
    owner_id: int = 1  # temporaire pour l'instant
):
    return create_project(session, payload, owner_id)


# --- PUT /projects/{project_id} ---
@router.put("/{project_id}", response_model=ProjectRead)
def edit_project_route(
    project_id: int,
    payload: ProjectUpdate,
    session: Session = Depends(get_session)
):
    return update_project(session, project_id, payload)


# --- DELETE /projects/{project_id} ---
@router.delete("/{project_id}")
def remove_project_route(
    project_id: int,
    session: Session = Depends(get_session)
):
    return delete_project(session, project_id)
