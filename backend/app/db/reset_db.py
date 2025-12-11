from sqlmodel import SQLModel
from app.db.session import engine
from app.models.user import User
from app.models.project import Project
from app.models.task import Task

def reset_database():
    print("🧹 Dropping all tables...")
    SQLModel.metadata.drop_all(bind=engine)  # supprime toutes les tables
    print("📦 Creating all tables...")
    SQLModel.metadata.create_all(bind=engine)  # recrée toutes les tables
    print("✅ Database reset complete!")