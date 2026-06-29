from app.agents.scorer import score_company


class ScoringService:

    @staticmethod
    def score(research: dict):

        return score_company(research)