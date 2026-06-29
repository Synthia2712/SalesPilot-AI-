import json

from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.prompts.scoring_prompt import SCORING_PROMPT


llm = ChatOpenAI(
    model=settings.OPENROUTER_MODEL,
    api_key=settings.OPENROUTER_API_KEY,
    base_url=settings.OPENROUTER_BASE_URL,
)


def score_company(research: dict):

    prompt = f"""
{SCORING_PROMPT}

Research:

{json.dumps(research, indent=2)}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)

    except Exception:
        return {
            "raw_response": response.content
        }