from app.tools.website_reader import WebsiteReader
from app.agents.researcher import research_company


class ResearchService:

    @staticmethod
    def analyze(company_name: str, website: str):

        website_text = WebsiteReader.read(website)

        research = research_company(
            company_name,
            website,
            website_text
        )

        return research