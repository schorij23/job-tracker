from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True)
    position = Column(String)
    status = Column(String)
    date_applied = Column(String)
    notes = Column(String)