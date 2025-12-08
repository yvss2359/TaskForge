from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectRead

router = APIRouter()

@router.get("/", response_model=list[ProjectRead])
def list_projects(skip: int = 0, limit: int = 50, session: Session = Depends(get_session)):
    projects = session.exec(select(Project).offset(skip).limit(limit)).all()
    return projects

@router.post("/", response_model=ProjectRead)
def create_project(payload: ProjectCreate, session: Session = Depends(get_session)):
    proj = Project(**payload.dict(), owner_id=1)  # temporaire: owner_id=1
    session.add(proj)
    session.commit()
    session.refresh(proj)
    return proj
