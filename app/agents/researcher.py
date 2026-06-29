import json

from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.prompts.research_prompt import RESEARCH_PROMPT


llm = ChatOpenAI(
    model=settings.OPENROUTER_MODEL,
    api_key=settings.OPENROUTER_API_KEY,
    base_url=settings.OPENROUTER_BASE_URL,
)


def research_company(company_name: str, website: str, website_text: str):

    prompt = f"""
{RESEARCH_PROMPT}

Company:
{company_name}

Website:
{website}

Website Content:
{website_text}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)

    except Exception:

        return {
            "raw_response": response.content
        }