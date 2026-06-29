from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


class Settings:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "google/gemini-2.5-pro"
    )

    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


settings = Settings()