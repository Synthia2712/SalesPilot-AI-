import json

from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.prompts.outreach_prompt import OUTREACH_PROMPT


llm = ChatOpenAI(
    model=settings.OPENROUTER_MODEL,
    api_key=settings.OPENROUTER_API_KEY,
    base_url=settings.OPENROUTER_BASE_URL,
    temperature=0.7,
    max_tokens=800,
)


def generate_email(research: dict):

    prompt = f"""
{OUTREACH_PROMPT}

Company Research:

{json.dumps(research, indent=2)}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)

    except Exception:

        return {
            "raw_response": response.content
        }