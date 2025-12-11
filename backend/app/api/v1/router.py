from fastapi import APIRouter

# Import des sous-routes
from app.api.v1 import projects,tasks,users

router = APIRouter()

# Inclusion des routes
router.include_router(projects.router, prefix="/projects", tags=["projects"])
router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
router.include_router(users.router, prefix="/users", tags=["users"])