from pydantic import BaseModel


class CompanyResearch(BaseModel):
    company_name: str
    website: str
    industry: str
    products: list[str]
    target_customers: list[str]
    pain_points: list[str]
    opportunities: list[str]
    summary: str