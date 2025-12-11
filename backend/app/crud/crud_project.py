from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


def get_projects(session: Session, skip: int = 0, limit: int = 50):
    return session.exec(
        select(Project)
        .offset(skip)
        .limit(limit)
        .options(selectinload(Project.tasks))
    ).all()


def get_project(session: Session, project_id: int):
    project = session.exec(
        select(Project).where(Project.id == project_id)
        .options(selectinload(Project.tasks))  # charger tasks
    ).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


def create_project(session: Session, payload: ProjectCreate, owner_id: int):
    project = Project(**payload.dict(), owner_id=owner_id)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def update_project(session: Session, project_id: int, payload: ProjectUpdate):
    project = get_project(session, project_id)

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(project, key, value)

    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def delete_project(session: Session, project_id: int):
    project = get_project(session, project_id)
    session.delete(project)
    session.commit()
    return {"ok": True}
