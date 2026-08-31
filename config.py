import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AgentModel:
    name: str
    provider: str
    model: str
    api_key: str


def secret(name: str) -> str:
    value = os.getenv(name, "").strip()

    if not value:
        raise RuntimeError(
            f"Missing GitHub secret/environment variable: {name}"
        )

    return value


# Each specialist gets its own credential and model.
MODELS = {
    "researcher": AgentModel(
        name="researcher",
        provider="groq",
        model=os.getenv("RESEARCHER_MODEL", "llama-3.3-70b-versatile"),
        api_key=secret("G"),
    ),

    "inventor": AgentModel(
        name="inventor",
        provider="groq",
        model=os.getenv("INVENTOR_MODEL", "llama-3.1-8b-instant"),
        api_key=secret("G1"),
    ),

    "scientist": AgentModel(
        name="scientist",
        provider="groq",
        model=os.getenv("SCIENTIST_MODEL", "llama-3.3-70b-versatile"),
        api_key=secret("G2"),
    ),

    "critic": AgentModel(
        name="critic",
        provider="openrouter",
        model=os.getenv(
            "CRITIC_MODEL",
            "google/gemini-2.5-flash"
        ),
        api_key=secret("OP"),
    ),

    "judge": AgentModel(
        name="judge",
        provider="openrouter",
        model=os.getenv(
            "JUDGE_MODEL",
            "deepseek/deepseek-chat"
        ),
        api_key=secret("OP2"),
    ),

    "strategist": AgentModel(
        name="strategist",
        provider="openrouter",
        model=os.getenv(
            "STRATEGIST_MODEL",
            "qwen/qwen3-30b-a3b"
        ),
        api_key=secret("OP3"),
    ),

    "gemini": AgentModel(
        name="gemini",
        provider="gemini",
        model=os.getenv(
            "GEMINI_MODEL",
            "gemini-3-flash"
        ),
        api_key=secret("GEM"),
    ),
}


def get_model(agent_name: str) -> AgentModel:
    try:
        return MODELS[agent_name]
    except KeyError:
        raise ValueError(f"Unknown agent model: {agent_name}")
