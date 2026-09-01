from crewai import LLM

from config import AgentModel


def create_llm(agent_model: AgentModel) -> LLM:
    """
    Transforme notre AgentModel en LLM CrewAI.

    Les clés API viennent exclusivement de config.py,
    donc des GitHub Secrets.
    """

    provider = agent_model.provider.lower().strip()
    model = agent_model.model.strip()

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
        api_key=agent_model.api_key,
    )