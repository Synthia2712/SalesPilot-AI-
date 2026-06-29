from fastapi import FastAPI

from app.api.agent import router as agent_router
from app.api.company import router as company_router
from app.api.export import router as export_router
from app.api.history import router as history_router
from app.api.outreach import router as outreach_router
from app.api.planner import router as planner_router
from app.api.research import router as research_router
from app.api.scoring import router as scoring_router

from app.database.init_db import create_database

create_database()

app = FastAPI(
    title="SalesPilot AI",
    description="Autonomous Sales Intelligence Platform",
    version="1.0.0",
)

app.include_router(planner_router)
app.include_router(company_router)
app.include_router(research_router)
app.include_router(scoring_router)
app.include_router(outreach_router)
app.include_router(agent_router)
app.include_router(history_router)
app.include_router(export_router)


@app.get("/")
def home():
    return {
        "message": "🚀 SalesPilot AI Running"
    }