from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job_schema import JobCreate

def get_jobs(db: Session):
    return db.query(Job).all()

def create_job(db: Session, job: JobCreate):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def delete_job(db: Session, job_id: int):
    job = db.query(Job).filter(Job.id == job_id).first()
    if job:
        db.delete(job)
        db.commit()
    return job