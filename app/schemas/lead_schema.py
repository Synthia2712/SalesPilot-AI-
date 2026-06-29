from pydantic import BaseModel


class LeadScore(BaseModel):
    company_name: str
    score: int
    reasons: list[str]
    recommendation: str