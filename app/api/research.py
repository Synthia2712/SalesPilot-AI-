from fastapi import APIRouter

from app.services.research_service import ResearchService

router = APIRouter(
    prefix="/research",
    tags=["Research"],
)


@router.get("/")
def research(
    company_name: str,
    website: str,
):

    result = ResearchService.analyze(
        company_name,
        website,
    )

    return {
        "research": result
    }