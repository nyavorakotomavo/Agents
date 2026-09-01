from crewai import LLM

from config import AgentModel


def _clean_api_key(value: str) -> str:
    if not value:
        raise ValueError("API key is empty")

    # Supprime espaces et retours à la ligne accidentels
    value = value.strip()

    # Supprime les caractères Unicode invisibles
    for char in (
        "\u200b",
        "\u200c",
        "\u200d",
        "\u200e",
        "\u200f",
        "\ufeff",
    ):
        value = value.replace(char, "")

    if not value:
        raise ValueError("API key is empty after cleaning")

    try:
        value.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError(
            "API key contains invalid Unicode characters"
        ) from exc

    return value


def create_llm(agent_model: AgentModel) -> LLM:
    provider = agent_model.provider.strip().lower()
    model = agent_model.model.strip()
    api_key = _clean_api_key(agent_model.api_key)

    if not model:
        raise ValueError(
            f"Model is empty for provider '{provider}'"
        )

    if provider == "groq":
        llm_model = f"groq/{model}"

    elif provider == "openrouter":
        llm_model = f"openrouter/{model}"

    elif provider == "gemini":
        llm_model = f"gemini/{model}"

    else:
        raise ValueError(
            f"Unsupported LLM provider: {agent_model.provider}"
        )

    return LLM(
        model=llm_model,
        api_key=api_key,
    )