from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.models import Company

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get("/")
def history():

    db = SessionLocal()

    companies = db.query(Company).all()

    result = []

    for company in companies:

        result.append(
            {
                "company": company.company_name,
                "website": company.website,
                "industry": company.industry,
                "score": company.score,
            }
        )

    db.close()

    return result