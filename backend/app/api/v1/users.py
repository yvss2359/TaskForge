from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session

from app.models.user import UserRead, UserCreate, UserUpdate
from app.crud.crud_user import (
    list_users,
    get_user,
    create_user,
    update_user,
    delete_user
)

router = APIRouter()

# --- GET /users/ ---
@router.get("/", response_model=list[UserRead])
def route_list_users(skip: int = 0, limit: int = 50, session: Session = Depends(get_session)):
    return list_users(session, skip, limit)

# --- GET /users/{id} ---
@router.get("/{user_id}", response_model=UserRead)
def route_get_user(user_id: int, session: Session = Depends(get_session)):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# --- POST /users/ ---
@router.post("/", response_model=UserRead)
def route_create_user(payload: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, payload)

# --- PUT /users/{id} ---
@router.put("/{user_id}", response_model=UserRead)
def route_update_user(user_id: int, payload: UserUpdate, session: Session = Depends(get_session)):
    user = update_user(session, user_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# --- DELETE /users/{id} ---
@router.delete("/{user_id}")
def route_delete_user(user_id: int, session: Session = Depends(get_session)):
    ok = delete_user(session, user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True}
