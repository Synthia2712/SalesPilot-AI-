from fastapi import APIRouter, Body

from app.services.outreach_service import OutreachService

router = APIRouter(
    prefix="/outreach",
    tags=["Outreach"],
)


@router.post("/")
def create_email(
    research: dict = Body(...)
):

    return OutreachService.generate(research)