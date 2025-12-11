from sqlmodel import Session, select
from app.models.user import User, UserCreate, UserUpdate

def list_users(session: Session, skip: int = 0, limit: int = 50):
    return session.exec(select(User).offset(skip).limit(limit)).all()

def get_user(session: Session, user_id: int):
    return session.get(User, user_id)

def create_user(session: Session, payload: UserCreate):
    user = User(
        email=payload.email,
        full_name=payload.full_name,
        is_active=True
        # ⚠️ password to be hashed later
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def update_user(session: Session, user_id: int, payload: UserUpdate):
    user = session.get(User, user_id)
    if not user:
        return None

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True
