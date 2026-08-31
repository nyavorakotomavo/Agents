from crewai import LLM

from config import AgentModel


def create_llm(agent_model: AgentModel) -> LLM:
    """
    Create a CrewAI LLM configured for one specific agent.

    Each agent can therefore use a different provider, model and API key.
    """

    provider = agent_model.provider.lower()

    if provider == "groq":
        return LLM(
            model=f"groq/{agent_model.model}",
            api_key=agent_model.api_key,
        )

    if provider == "openrouter":
        return LLM(
            model=f"openrouter/{agent_model.model}",
            api_key=agent_model.api_key,
        )

    if provider == "gemini":
        return LLM(
            model=f"gemini/{agent_model.model}",
            api_key=agent_model.api_key,
        )

    raise ValueError(
        f"Unsupported LLM provider: {agent_model.provider}"
    )