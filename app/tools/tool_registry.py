from app.services.company_service import CompanyService
from app.services.research_service import ResearchService
from app.services.scoring_service import ScoringService
from app.services.outreach_service import OutreachService

class ToolRegistry:

    @staticmethod
    def execute(tool: str, data: dict):

        if tool == "company_search":
            return CompanyService().search(
                data["query"]
            )

        elif tool == "research":
            return ResearchService.analyze(
                data["company_name"],
                data["website"]
            )

        elif tool == "lead_scoring":
            return ScoringService.score(
                data["research"]
            )
        elif tool == "outreach":

            return OutreachService.generate(
                data["research"]
            ) 
        
        else:
            raise Exception(f"Unknown tool: {tool}")