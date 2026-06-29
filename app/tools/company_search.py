from tavily import TavilyClient

from app.core.config import settings


class CompanySearchTool:

    def __init__(self):
        self.client = TavilyClient(
            api_key=settings.TAVILY_API_KEY
        )

    def run(self, query: str):

        response = self.client.search(
            query=query,
            max_results=5,
        )

        companies = []

        for result in response.get("results", []):

            companies.append({
                "name": result.get("title", ""),
                "website": result.get("url", ""),
                "summary": result.get("content", ""),
                "source": "Tavily"
            })

        return companies