from typing import Optional
from sqlmodel import SQLModel

class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    status: str = "todo"

class TaskCreate(TaskBase):
    pass  # pas de project_id ici

class TaskRead(TaskBase):
    id: int
    project_id: int

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
