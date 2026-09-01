from crewai import LLM

from config import AgentModel


def _clean_api_key(value: str) -> str:
    """Nettoie les caractères invisibles accidentellement copiés dans une clé."""
    if not value:
        raise ValueError("API key is empty")

    # Les clés API utilisées ici doivent être ASCII.
    cleaned = value.strip()

    # Supprime les caractères Unicode invisibles/fréquemment copiés
    invisible = (
        "\u200b",  # zero-width space
        "\u200c",  # zero-width non-joiner
        "\u200d",  # zero-width joiner
        "\u200e",  # left-to-right mark
        "\u200f",  # right-to-left mark
        "\ufeff",  # BOM
    )

    for char in invisible:
        cleaned = cleaned.replace(char, "")

    try:
        cleaned.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError(
            "API key contains an unsupported Unicode character. "
            "Check the corresponding GitHub Secret."
        ) from exc

    return cleaned


def create_llm(agent_model: AgentModel) -> LLM:
    provider = agent_model.provider.lower().strip()
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