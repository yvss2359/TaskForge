from faker import Faker
import random
from app.db.session import get_session
from app.models.user import User
from app.models.project import Project
from app.models.task import Task

fake = Faker()

def seed_database():
    print("🌱 Seeding database with fake data...")
    session = next(get_session())  # récupère la session SQLAlchemy

    # --- USERS ---
    users = []
    for _ in range(10):
        user = User(
            email=fake.unique.email(),
            full_name=fake.name(),
            is_active=True
        )
        users.append(user)
    session.add_all(users)
    session.commit()
    for user in users:
        session.refresh(user)

    # --- PROJECTS ---
    projects = []
    for user in users:
        for _ in range(random.randint(5, 10)):
            project = Project(
                name=fake.catch_phrase(),
                description=fake.sentence(nb_words=6),
                owner_id=user.id
            )
            projects.append(project)
    session.add_all(projects)
    session.commit()
    for project in projects:
        session.refresh(project)

    # --- TASKS ---
    tasks = []
    statuses = ["todo", "in_progress", "done"]
    for project in projects:
        for _ in range(random.randint(3, 7)):
            task = Task(
                title=fake.sentence(nb_words=4),
                description=fake.sentence(nb_words=10),
                status=random.choice(statuses),
                project_id=project.id
            )
            tasks.append(task)
    session.add_all(tasks)
    session.commit()
    for task in tasks:
        session.refresh(task)

    print("✅ Database seeded successfully with fake users, projects, and tasks!")