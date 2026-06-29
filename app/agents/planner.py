import json

from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.prompts.planner_prompt import PLANNER_PROMPT


llm = ChatOpenAI(
    model=settings.OPENROUTER_MODEL,
    api_key=settings.OPENROUTER_API_KEY,
    base_url=settings.OPENROUTER_BASE_URL,
    temperature=0,
    max_tokens=1000,
)


def generate_plan(query: str):

    prompt = f"""
{PLANNER_PROMPT}

User Goal:

{query}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)

    except Exception:
        # Fallback plan if the LLM returns invalid JSON
        return {
            "goal": query,
            "tasks": [
                {
                    "tool": "company_search",
                    "input": query
                },
                {
                    "tool": "research"
                },
                {
                    "tool": "lead_scoring"
                },
                {
                    "tool": "outreach"
                }
            ]
        }