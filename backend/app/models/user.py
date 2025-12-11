from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class UserBase(SQLModel):
    email: str
    full_name: Optional[str] = None
    is_active: bool = True

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    full_name: Optional[str] = None
    is_active: bool = True

    # Relationship towards projects
    projects: List["Project"] = Relationship(back_populates="owner")

class UserCreate(UserBase):
    password: str  # stocks only a hashed password (later implementation)

class UserRead(UserBase):
    id: int

class UserUpdate(SQLModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.project import Project
