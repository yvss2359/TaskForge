from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str

class ProjectRead(ProjectCreate):
    id: int
    owner_id: int
