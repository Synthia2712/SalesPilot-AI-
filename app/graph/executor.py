from concurrent.futures import ThreadPoolExecutor, as_completed

from app.core.logger import logger
from app.database.crud import CompanyCRUD
from app.services.planner_service import PlannerService
from app.tools.tool_registry import ToolRegistry


class ExecutionEngine:

    @staticmethod
    def execute(user_query: str):

        logger.info("=" * 60)
        logger.info("SalesPilot Execution Started")

        plan = PlannerService.create_plan(user_query)

        companies = ToolRegistry.execute(
            "company_search",
            {
                "query": user_query
            }
        )

        logger.info(f"Found {len(companies)} companies")

        def process_company(company):

            website = company.get("website", "").strip()

            if not website:
                return None

            try:

                research = ToolRegistry.execute(
                    "research",
                    {
                        "company_name": company["name"],
                        "website": website,
                    },
                )

                score = ToolRegistry.execute(
                    "lead_scoring",
                    {
                        "research": research
                    },
                )

                outreach = ToolRegistry.execute(
                    "outreach",
                    {
                        "research": research
                    },
                )

                CompanyCRUD.save(
                    company,
                    research,
                    score,
                    outreach
                )

                logger.info(f"Saved {company['name']}")

                return {
                    "company": company,
                    "research": research,
                    "score": score,
                    "outreach": outreach,
                }

            except Exception as e:

                logger.error(str(e))

                return {
                    "company": company,
                    "error": str(e)
                }

        results = []

        with ThreadPoolExecutor(max_workers=5) as executor:

            futures = [
                executor.submit(process_company, company)
                for company in companies
            ]

            for future in as_completed(futures):

                result = future.result()

                if result:
                    results.append(result)

        logger.info("Execution Complete")

        return {
            "goal": plan["goal"],
            "results": results
        }