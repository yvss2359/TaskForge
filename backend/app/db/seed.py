from app.db.session import get_session
from app.models.user import User
from app.models.project import Project
from app.models.task import Task

def seed_database():
    print("🌱 Seeding database...")
    session = next(get_session())  # <-- utilise next() pour récupérer la session du générateur

    # --- USERS ---
    users_data = [
        {"email": "admin@example.com", "full_name": "Admin User", "is_active": True},
        {"email": "john@example.com", "full_name": "John Doe", "is_active": True},
        {"email": "jane@example.com", "full_name": "Jane Doe", "is_active": True},
    ]
    users = [User(**data) for data in users_data]
    session.add_all(users)
    session.commit()
    for user in users:
        session.refresh(user)

    # --- PROJECTS ---
    projects_data = [
        {"name": "Project Alpha", "description": "First project", "owner_id": users[0].id},
        {"name": "Project Beta", "description": "Second project", "owner_id": users[1].id},
        {"name": "Project Gamma", "description": "Third project", "owner_id": users[2].id},
    ]
    projects = [Project(**data) for data in projects_data]
    session.add_all(projects)
    session.commit()
    for project in projects:
        session.refresh(project)

    # --- TASKS ---
    tasks_data = [
        {"title": "Setup FastAPI", "description": "Configure backend", "status": "todo", "project_id": projects[0].id},
        {"title": "Create Models", "description": "Define User, Project, Task", "status": "todo", "project_id": projects[0].id},
        {"title": "Build Angular UI", "description": "Frontend initial layout", "status": "todo", "project_id": projects[1].id},
        {"title": "Implement CRUD", "description": "Tasks and Projects API", "status": "in_progress", "project_id": projects[1].id},
        {"title": "Write Tests", "description": "Unit tests for backend", "status": "todo", "project_id": projects[2].id},
    ]
    tasks = [Task(**data) for data in tasks_data]
    session.add_all(tasks)
    session.commit()
    for task in tasks:
        session.refresh(task)

    print("✅ Database seeded successfully!")