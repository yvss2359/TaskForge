from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str = "taskforge"
    POSTGRES_PASSWORD: str = "taskforge"
    POSTGRES_DB: str = "taskforge"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    # Important : URL SQLAlchemy complète
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = ".env"

settings = Settings()
