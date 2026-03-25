from fastapi import FastAPI
from app.routes import job_routes
from app.db.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker")

# Include routes
app.include_router(job_routes.router)

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}