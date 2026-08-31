from crewai.tools import tool
import requests


@tool("Web Search")
def web_search(query: str) -> str:
    """
    Search the web for recent information.

    This is intentionally a lightweight first version.
    A dedicated search provider can be connected later.
    """
    query = query.strip()

    if not query:
        return "ERROR: Empty search query."

    url = "https://www.google.com/search"
    params = {"q": query}

    try:
        response = requests.get(
            url,
            params=params,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (compatible; AutonomousAgents/1.0)"
                )
            },
            timeout=15,
        )

        response.raise_for_status()

        # Return only a limited amount of text to avoid flooding the LLM.
        text = response.text
        return text[:12000]

    except requests.RequestException as exc:
        return f"SEARCH_ERROR: {exc}"