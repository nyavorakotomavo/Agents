import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AgentModel:
    name: str
    provider: str
    model: str
    api_key: str


def secret(name: str) -> str:
    """
    Récupère UNIQUEMENT une clé API depuis les variables
    d'environnement / GitHub Secrets.
    """
    value = os.getenv(name, "").strip()

    if not value or value == "***":
        raise RuntimeError(
            f"Missing or invalid GitHub secret/environment variable: {name}"
        )

    return value


# ============================================================
# 7 AGENTS / CONFIGURATION DES MODÈLES
# ============================================================

MODELS = {

    # --------------------------------------------------------
    # 1. GLOBAL RESEARCHER
    # --------------------------------------------------------
    "researcher": AgentModel(
        name="researcher",
        provider="groq",
        model="openai/gpt-oss-120b",
        api_key=secret("G"),
    ),

    # --------------------------------------------------------
    # 2. RADICAL INVENTOR
    # --------------------------------------------------------
    "inventor": AgentModel(
        name="inventor",
        provider="groq",
        model="openai/gpt-oss-20b",
        api_key=secret("G1"),
    ),

    # --------------------------------------------------------
    # 3. SCIENTIFIC THINKER
    # --------------------------------------------------------
    "scientist": AgentModel(
        name="scientist",
        provider="groq",
        model="openai/gpt-oss-120b",
        api_key=secret("G2"),
    ),

    # --------------------------------------------------------
    # 4. ADVERSARIAL CRITIC (Double rôle : Clé GEM)
    # --------------------------------------------------------
    "critic": AgentModel(
        name="critic",
        provider="gemini",
        model="gemini-3.6-flash",
        api_key=secret("GEM"),
    ),

    # --------------------------------------------------------
    # 5. INNOVATION JUDGE
    # --------------------------------------------------------
    "judge": AgentModel(
        name="judge",
        provider="openrouter",
        model="deepseek/deepseek-chat",
        api_key=secret("OP2"),
    ),

    # --------------------------------------------------------
    # 6. STRATEGIST
    # --------------------------------------------------------
    "strategist": AgentModel(
        name="strategist",
        provider="openrouter",
        model="openai/gpt-oss-120b",
        api_key=secret("OP3"),
    ),

    # --------------------------------------------------------
    # 7. GEMINI
    # --------------------------------------------------------
    "gemini": AgentModel(
        name="gemini",
        provider="gemini",
        model="gemini-3.6-flash",
        api_key=secret("GEM"),
    ),
}


def get_model(agent_name: str) -> AgentModel:
    """
    Retourne la configuration du modèle demandé.
    """
    try:
        return MODELS[agent_name]
    except KeyError:
        available = ", ".join(MODELS.keys())
        raise ValueError(
            f"Unknown agent model: {agent_name}. "
            f"Available models: {available}"
        )
