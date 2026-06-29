from pydantic import BaseModel
from typing import List


class Task(BaseModel):
    id: int
    tool: str
    input: str


class PlannerResponse(BaseModel):
    goal: str
    tasks: List[Task]