from sqlmodel import SQLModel

# Importer TOUS les modèles ici pour que Alembic les détecte
from app.models.project import Project
from app.models.task import Task
