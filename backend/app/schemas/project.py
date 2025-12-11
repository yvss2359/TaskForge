from typing import Optional, List
from sqlmodel import SQLModel
from app.schemas.task import TaskRead

class ProjectBase(SQLModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectRead(ProjectBase):
    id: int
    # Pour l’instant on peut ignorer la relation tasks ou la mettre optionnelle
    tasks: Optional[List[TaskRead]] = None

class ProjectUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
