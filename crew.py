import os
from crewai import Agent, Crew, Process, Task

def create_autonomous_crew(topic: str = "AI Automation") -> Crew:
    """
    Creates and returns a CrewAI Crew configured with agents and tasks.
    """
    researcher = Agent(
        role="Research Analyst",
        goal=f"Analyze and gather information on {topic}",
        backstory="An expert researcher capable of analyzing complex trends and synthesizing actionable insights.",
        verbose=True,
        allow_delegation=False
    )

    writer = Agent(
        role="Content Strategist",
        goal=f"Create a concise summary report based on research about {topic}",
        backstory="A skilled communicator who transforms detailed analytical data into clear, engaging summaries.",
        verbose=True,
        allow_delegation=False
    )

    research_task = Task(
        description=f"Conduct a comprehensive analysis of {topic}. Identify key trends and opportunities.",
        expected_output="A bullet-point summary of key trends and opportunities.",
        agent=researcher
    )

    writing_task = Task(
        description=f"Using the findings from the research task, draft a final executive report on {topic}.",
        expected_output="A clean, structured executive summary report.",
        agent=writer
    )

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True
    )

    return crew

def run_crew(topic: str = "AI Automation") -> str:
    """
    Instantiates and executes the crew for a given topic.
    Returns the final output as a string.
    """
    crew = create_autonomous_crew(topic=topic)
    result = crew.kickoff()
    return str(result)

if __name__ == "__main__":
    output = run_crew("Autonomous Agents with CrewAI")
    print("Execution Output:\n", output)
