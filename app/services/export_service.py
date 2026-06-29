import pandas as pd

from app.database.database import SessionLocal
from app.database.models import Company


class ExportService:

    @staticmethod
    def export():

        db = SessionLocal()

        companies = db.query(Company).all()

        rows = []

        for company in companies:

            rows.append(
                {
                    "Company": company.company_name,
                    "Website": company.website,
                    "Industry": company.industry,
                    "Score": company.score,
                    "Summary": company.summary,
                    "Email": company.email,
                }
            )

        db.close()

        df = pd.DataFrame(rows)

        filename = "salespilot_export.xlsx"

        df.to_excel(
            filename,
            index=False,
        )

        return filename