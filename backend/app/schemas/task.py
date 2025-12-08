from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str

class TaskRead(TaskCreate):
    id: int
    owner_id: int
