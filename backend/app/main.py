from fastapi import FastAPI
from app.api.v1.router import router as api_router 

app = FastAPI(
    title="TaskForge API",
    version="1.0.0",
    description="Backend FastAPI pour le projet TaskForge"
)

# inclure tous les routers
app.include_router(api_router, prefix="/api/v1")

# simple health check
@app.get("/health")
def health_check():
    return {"status": "ok"}

# lancment de l'API
@app.get("/")
def root():
    return {"message": "TaskForge API is running!"}
