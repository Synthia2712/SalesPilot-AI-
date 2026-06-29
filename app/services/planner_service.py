from app.graph.graph import graph


class PlannerService:

    @staticmethod
    def create_plan(query: str):

        result = graph.invoke(
            {
                "query": query
            }
        )

        return result["plan"]