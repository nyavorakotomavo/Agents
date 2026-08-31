import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """
    Configuration centrale du laboratoire d'agents.

    Les secrets ne sont jamais écrits directement dans le code.
    Ils seront fournis plus tard par GitHub Secrets / Variables.
    """

    model: str = os.getenv("MODEL", "gpt-4o-mini")
    max_iterations: int = int(os.getenv("MAX_ITERATIONS", "3"))
    max_ideas: int = int(os.getenv("MAX_IDEAS", "10"))
    research_depth: int = int(os.getenv("RESEARCH_DEPTH", "2"))
    output_dir: str = os.getenv("OUTPUT_DIR", "outputs")

    @property
    def llm_api_key(self) -> str | None:
        """
        Récupère la clé du fournisseur LLM sans jamais l'afficher.
        """
        return os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")


settings = Settings()