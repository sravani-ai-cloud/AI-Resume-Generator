from pydantic import BaseModel


class ResumeRequest(BaseModel):
    name: str
    experience: int
    skills: list[str]