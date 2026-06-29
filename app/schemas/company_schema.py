from pydantic import BaseModel


class Company(BaseModel):
    name: str
    website: str
    summary: str
    source: str