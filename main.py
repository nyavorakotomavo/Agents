from config import MODELS

print("=== MODEL CONFIGURATION ===")

for name, cfg in MODELS.items():
    print(
        f"{name}: provider={cfg.provider}, model={cfg.model}"
    )

print("===========================")
import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from crew import run_crew


app = FastAPI(title="Autonomous Agents")


class CrewRequest(BaseModel):
    objective: str = "Trouver une idée révolutionnaire de site ou application"


def run_objective(objective: str) -> str:
    """Run the autonomous discovery crew for an objective."""
    return run_crew(objective)


@app.get("/")
def home():
    return {
        "status": "online",
        "system": "Autonomous Agents",
        "message": "The autonomous laboratory is online 🚀",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/run")
def execute_crew(request: CrewRequest):
    objective = request.objective.strip()

    if not objective:
        raise HTTPException(
            status_code=400,
            detail="Objective cannot be empty.",
        )

    try:
        result = run_objective(objective)

        return {
            "status": "success",
            "objective": objective,
            "result": result,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {exc}",
        )


def run_from_github_actions():
    """
    Execute an objective supplied by GitHub Actions.

    The result is written to outputs/latest_result.txt so that
    GitHub Actions can preserve it as an artifact.
    """
    objective = os.getenv(
        "OBJECTIVE",
        "Trouver une idée révolutionnaire de site ou application",
    ).strip()

    if not objective:
        objective = "Trouver une idée révolutionnaire de site ou application"

    result = run_objective(objective)

    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    result_file = output_dir / "latest_result.txt"

    result_file.write_text(
        f"OBJECTIVE\n{objective}\n\nRESULT\n{result}\n",
        encoding="utf-8",
    )

    print(f"Objective completed: {objective}")
    print(f"Result saved to: {result_file}")


if __name__ == "__main__":
    run_from_github_actions()