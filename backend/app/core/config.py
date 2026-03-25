import os

class Settings:
    PROJECT_NAME: str = "Job Tracker"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./jobs.db")

settings = Settings()