from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str

class UserRead(UserCreate):
    id: int
    owner_id: int
