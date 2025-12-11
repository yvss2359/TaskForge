from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None

    # Forghien key towards User
    owner_id: int = Field(foreign_key="users.id")
    owner: Optional["User"] = Relationship(back_populates="projects")
    
    # Relationship towards Task (forward reference)
    tasks: list["Task"] = Relationship(
        back_populates="project",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.user import User
    from app.models.task import Task