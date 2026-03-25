from pydantic import BaseModel

class JobBase(BaseModel):
    company: str
    position: str
    status: str
    date_applied: str
    notes: str

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True