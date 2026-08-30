from fastapi import FastAPI

app = FastAPI(title="Autonomous Agents")

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Autonomous Agents is running 🚀"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}