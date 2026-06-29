from fastapi import APIRouter, Body

from app.services.scoring_service import ScoringService

router = APIRouter(
    prefix="/scoring",
    tags=["Lead Scoring"],
)


@router.post("/")
def score_company_api(
    research: dict = Body(...)
):

    result = ScoringService.score(research)

    return result