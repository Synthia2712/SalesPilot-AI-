from fastapi import APIRouter

from app.graph.executor import ExecutionEngine

router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"],
)


@router.get("/run")
def run_agent(query: str):

    result = ExecutionEngine.execute(query)

    return {
        "query": query,
        "results": result
    }