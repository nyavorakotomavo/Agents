from unittest.mock import patch, MagicMock
from crew import create_autonomous_crew, run_crew

def test_create_autonomous_crew():
    topic = "Software Engineering Automation"
    crew = create_autonomous_crew(topic=topic)

    assert len(crew.agents) == 2
    assert len(crew.tasks) == 2
    assert crew.agents[0].role == "Research Analyst"
    assert crew.agents[1].role == "Content Strategist"

@patch("crew.Crew.kickoff")
def test_run_crew(mock_kickoff):
    mock_kickoff.return_value = "Agent task finished successfully."
    result = run_crew("AI Testing")
    assert result == "Agent task finished successfully."
    mock_kickoff.assert_called_once()
