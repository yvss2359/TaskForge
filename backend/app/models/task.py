from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    status: str = "todo"
    project_id: int = Field(foreign_key="project.id")

    # Reverse relationship towards Project (forward reference)
    project: Optional["Project"] = Relationship(back_populates="tasks")

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.project import Project
