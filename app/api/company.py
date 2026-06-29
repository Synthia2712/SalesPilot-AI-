from fastapi import APIRouter

from app.services.company_service import CompanyService

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)

service = CompanyService()


@router.get("/search")
def search_companies(query: str):

    companies = service.search(query)

    return {
        "count": len(companies),
        "companies": companies
    }