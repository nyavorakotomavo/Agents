from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "online",
        "message": "Autonomous Agents is running 🚀"
    }

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@patch("main.run_crew")
def test_run_crew_endpoint(mock_run_crew):
    mock_run_crew.return_value = "Mocked execution output"
    response = client.post("/run-crew", json={"topic": "Test Topic"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "topic": "Test Topic",
        "output": "Mocked execution output"
    }
    mock_run_crew.assert_called_once_with(topic="Test Topic")
