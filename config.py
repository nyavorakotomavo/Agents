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


# ============================================================
# MODELES DES 7 AGENTS
# ============================================================
#
# IMPORTANT :
# Les modèles Groq utilisés ici sont des modèles actuellement
# disponibles dans l'API Groq.
#
# On évite volontairement llama-3.1-70b-versatile et
# llama-3.3-70b-versatile.
# ============================================================

MODELS = {

    # --------------------------------------------------------
    # 1. GLOBAL RESEARCHER
    # --------------------------------------------------------
    "researcher": AgentModel(
        name="researcher",
        provider="groq",
        model=os.getenv(
            "RESEARCHER_MODEL",
            "openai/gpt-oss-120b"
        ),
        api_key=secret("G"),
    ),

    # --------------------------------------------------------
    # 2. INVENTOR
    # --------------------------------------------------------
    "inventor": AgentModel(
        name="inventor",
        provider="groq",
        model=os.getenv(
            "INVENTOR_MODEL",
            "openai/gpt-oss-20b"
        ),
        api_key=secret("G1"),
    ),

    # --------------------------------------------------------
    # 3. SCIENTIST
    # --------------------------------------------------------
    "scientist": AgentModel(
        name="scientist",
        provider="groq",
        model=os.getenv(
            "SCIENTIST_MODEL",
            "llama-3.1-8b-instant"
        ),
        api_key=secret("G2"),
    ),

    # --------------------------------------------------------
    # 4. CRITIC
    # --------------------------------------------------------
    "critic": AgentModel(
        name="critic",
        provider="openrouter",
        model=os.getenv(
            "CRITIC_MODEL",
            "google/gemini-2.5-flash"
        ),
        api_key=secret("OP"),
    ),

    # --------------------------------------------------------
    # 5. JUDGE
    # --------------------------------------------------------
    "judge": AgentModel(
        name="judge",
        provider="openrouter",
        model=os.getenv(
            "JUDGE_MODEL",
            "deepseek/deepseek-chat"
        ),
        api_key=secret("OP2"),
    ),

    # --------------------------------------------------------
    # 6. STRATEGIST
    # --------------------------------------------------------
    "strategist": AgentModel(
        name="strategist",
        provider="openrouter",
        model=os.getenv(
            "STRATEGIST_MODEL",
            "qwen/qwen3-30b-a3b"
        ),
        api_key=secret("OP3"),
    ),

    # --------------------------------------------------------
    # 7. GEMINI
    # --------------------------------------------------------
    "gemini": AgentModel(
        name="gemini",
        provider="gemini",
        model=os.getenv(
            "GEMINI_MODEL",
            "gemini-2.0-flash"
        ),
        api_key=secret("GEM"),
    ),
}


def get_model(agent_name: str) -> AgentModel:
    try:
        return MODELS[agent_name]
    except KeyError:
        raise ValueError(
            f"Unknown agent model: {agent_name}"
        )