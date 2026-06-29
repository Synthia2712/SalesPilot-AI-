from app.agents.outreach import generate_email


class OutreachService:

    @staticmethod
    def generate(research: dict):

        return generate_email(research)