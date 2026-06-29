from fastapi import APIRouter

from app.services.planner_service import PlannerService

router = APIRouter(
    prefix="/planner",
    tags=["Planner"],
)


@router.get("/plan")
def plan(query: str):

    result = PlannerService.create_plan(query)

    return {
        "success": True,
        "query": query,
        "plan": result,
    }