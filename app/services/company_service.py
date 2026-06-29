from app.tools.company_search import CompanySearchTool


class CompanyService:

    def __init__(self):
        self.tool = CompanySearchTool()

    def search(self, query: str):
        return self.tool.run(query)