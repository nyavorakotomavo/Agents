from crewai import LLM

from config import AgentModel


def create_llm(agent_model: AgentModel) -> LLM:
    provider = agent_model.provider.lower()

    if provider == "groq":
        model = f"groq/{agent_model.model}"

    elif provider == "openrouter":
        model = f"openrouter/{agent_model.model}"

    elif provider == "gemini":
        model = f"gemini/{agent_model.model}"

    else:
        raise ValueError(
            f"Unsupported LLM provider: {agent_model.provider}"
        )

    return LLM(
        model=model,
        api_key=agent_model.api_key,
    )