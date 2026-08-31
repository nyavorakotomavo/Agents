import crewai.llms.cache as _crewai_cache

_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from crewai import Agent, Crew, Process, Task
from crewai import Agent, Crew, Process, Task

from config import get_model
from llm_factory import create_llm


def create_autonomous_crew(
    topic: str = "revolutionary technology",
) -> Crew:

    researcher = Agent(
        role="Global Researcher",
        goal=(
            f"Investigate the world around '{topic}'. Identify emerging "
            "technologies, important problems, changing behaviors, market "
            "gaps and overlooked opportunities."
        ),
        backstory=(
            "You are a multidisciplinary researcher. You look for weak "
            "signals and connections that ordinary analysis misses."
        ),
        llm=create_llm(get_model("researcher")),
        verbose=True,
        allow_delegation=False,
    )

    inventor = Agent(
        role="Radical Inventor",
        goal=(
            f"Create original and potentially transformative solutions "
            f"related to '{topic}'. Combine distant fields and challenge "
            "common assumptions."
        ),
        backstory=(
            "You are an unconventional inventor who searches for unusual "
            "combinations of technologies and human needs."
        ),
        llm=create_llm(get_model("inventor")),
        verbose=True,
        allow_delegation=False,
    )

    scientist = Agent(
        role="Scientific Thinker",
        goal=(
            f"Analyze '{topic}' using first-principles reasoning. "
            "Discover hidden assumptions, fundamental mechanisms and "
            "unexpected possibilities."
        ),
        backstory=(
            "You use rigorous reasoning, abstraction and thought experiments "
            "to investigate problems."
        ),
        llm=create_llm(get_model("scientist")),
        verbose=True,
        allow_delegation=False,
    )

    critic = Agent(
        role="Adversarial Critic",
        goal=(
            "Attack proposed ideas. Identify competitors, technical "
            "obstacles, weak assumptions, economic problems and reasons "
            "each idea could fail."
        ),
        backstory=(
            "You are an aggressive skeptic. You search for weaknesses "
            "before the team invests resources."
        ),
        llm=create_llm(get_model("critic")),
        verbose=True,
        allow_delegation=False,
    )

    judge = Agent(
        role="Innovation Judge",
        goal=(
            "Evaluate the strongest ideas according to originality, "
            "problem severity, market size, feasibility, monetization, "
            "defensibility and growth potential."
        ),
        backstory=(
            "You are the final evaluator. You prefer ideas with large "
            "real-world impact and realistic implementation paths."
        ),
        llm=create_llm(get_model("judge")),
        verbose=True,
        allow_delegation=False,
    )

    research_task = Task(
        description=(
            f"Investigate '{topic}' and identify at least 10 meaningful "
            "signals, problems, trends, inefficiencies or opportunities."
        ),
        expected_output=(
            "A structured report containing at least 10 signals and "
            "why each could matter."
        ),
        agent=researcher,
    )

    invention_task = Task(
        description=(
            "Using the research, generate at least 15 distinct ideas. "
            "For every idea describe the problem, users, solution and "
            "what makes the approach unusual."
        ),
        expected_output=(
            "At least 15 structured concepts with problem, users, solution "
            "and originality rationale."
        ),
        agent=inventor,
        context=[research_task],
    )

    science_task = Task(
        description=(
            "Analyze the research and proposed ideas using first-principles "
            "reasoning. Identify overlooked opportunities and propose "
            "additional concepts when appropriate."
        ),
        expected_output=(
            "Rigorous analysis of fundamental principles and overlooked "
            "opportunities."
        ),
        agent=scientist,
        context=[research_task, invention_task],
    )

    criticism_task = Task(
        description=(
            "Aggressively challenge the proposed ideas. Examine competition, "
            "technical feasibility, user demand, economics and failure modes."
        ),
        expected_output=(
            "Critical evaluation of the strongest concepts and their "
            "main weaknesses."
        ),
        agent=critic,
        context=[
            research_task,
            invention_task,
            science_task,
        ],
    )

    judgment_task = Task(
        description=(
            "Select the three strongest opportunities. Score each from 0 "
            "to 10 for originality, problem severity, market size, "
            "feasibility, monetization, defensibility and growth potential. "
            "Choose one final winner and propose its MVP."
        ),
        expected_output=(
            "A ranked top-three list with scores, followed by one final "
            "recommendation and an MVP direction."
        ),
        agent=judge,
        context=[
            research_task,
            invention_task,
            science_task,
            criticism_task,
        ],
    )

    return Crew(
        agents=[
            researcher,
            inventor,
            scientist,
            critic,
            judge,
        ],
        tasks=[
            research_task,
            invention_task,
            science_task,
            criticism_task,
            judgment_task,
        ],
        process=Process.sequential,
        verbose=True,
    )


def run_crew(topic: str = "revolutionary technology") -> str:
    crew = create_autonomous_crew(topic)
    result = crew.kickoff()
    return str(result)


if __name__ == "__main__":
    print(run_crew())