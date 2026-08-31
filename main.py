from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from crew import run_crew

app = FastAPI(title="Autonomous Agents with CrewAI")

class CrewRequest(BaseModel):
    topic: str = "AI Automation"

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Autonomous Agents is running 🚀"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/run-crew")
def execute_crew(request: CrewRequest):
    try:
        output = run_crew(topic=request.topic)
        return {
            "status": "success",
            "topic": request.topic,
            "output": output
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
