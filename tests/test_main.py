from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "online",
        "system": "Autonomous Agents",
        "message": "The autonomous laboratory is online 🚀",
    }

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@patch("main.run_objective")
def test_execute_crew_endpoint(mock_run_objective):
    mock_run_objective.return_value = "Mocked execution output"
    response = client.post("/run", json={"objective": "Test Objective"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "objective": "Test Objective",
        "result": "Mocked execution output",
    }
    mock_run_objective.assert_called_once_with("Test Objective")
