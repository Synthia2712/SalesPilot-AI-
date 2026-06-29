from app.database.database import SessionLocal
from app.database.models import Company


class CompanyCRUD:

    @staticmethod
    def save(company, research, score, outreach):

        db = SessionLocal()

        try:

            row = Company(
                company_name=company.get("name", ""),
                website=company.get("website", ""),
                industry=research.get("industry", ""),
                summary=research.get("summary", ""),
                score=score.get("score", 0),
                email=outreach.get("email", "")
            )

            db.add(row)
            db.commit()

        finally:
            db.close()