import requests
from bs4 import BeautifulSoup


class WebsiteReader:

    @staticmethod
    def read(url: str) -> str:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            # Remove unwanted tags
            for tag in soup(
                [
                    "script",
                    "style",
                    "noscript",
                    "svg",
                    "footer",
                    "header",
                    "nav"
                ]
            ):
                tag.decompose()

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return text[:12000]

        except Exception as e:
            return f"Error reading website: {e}"