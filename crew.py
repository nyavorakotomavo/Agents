from crewai import Agent, Crew, Process, Task


def create_autonomous_crew(topic: str = "revolutionary technology") -> Crew:
    """
    Creates the first version of the Autonomous Discovery Lab.

    The crew is deliberately separated into different cognitive roles:
    research, invention, scientific reasoning, criticism and evaluation.
    """

    researcher = Agent(
        role="Global Researcher",
        goal=(
            f"Investigate the current world around '{topic}'. "
            "Identify emerging technologies, major trends, unsolved problems, "
            "new user behaviors, market gaps and important contradictions."
        ),
        backstory=(
            "You are an extremely curious multidisciplinary researcher. "
            "You do not simply summarize popular information. "
            "You search for signals that could reveal opportunities that "
            "most people have not noticed yet."
        ),
        verbose=True,
        allow_delegation=False,
    )

    inventor = Agent(
        role="Radical Inventor",
        goal=(
            f"Generate original and potentially transformative ideas related to "
            f"'{topic}'. Combine distant fields, challenge assumptions and "
            "look for solutions that could become globally useful products."
        ),
        backstory=(
            "You are an unconventional inventor. You deliberately question "
            "ordinary solutions and explore combinations between unrelated "
            "technologies, industries and human needs."
        ),
        verbose=True,
        allow_delegation=False,
    )

    scientist = Agent(
        role="Scientific Thinker",
        goal=(
            f"Analyze '{topic}' using rigorous reasoning. "
            "Look for fundamental principles, unexplained observations, "
            "hidden assumptions and opportunities for new approaches."
        ),
        backstory=(
            "You are a multidisciplinary scientific thinker inspired by the "
            "problem-solving approaches of historical scientists and inventors. "
            "You do not imitate personalities; you use methods such as "
            "thought experiments, abstraction, first-principles reasoning "
            "and systematic observation."
        ),
        verbose=True,
        allow_delegation=False,
    )

    critic = Agent(
        role="Adversarial Critic",
        goal=(
            "Attack every proposed idea. Find existing competitors, obvious "
            "solutions, technical obstacles, economic weaknesses, legal risks, "
            "poor assumptions and reasons the idea could fail."
        ),
        backstory=(
            "You are the team's strongest skeptic. Your job is not to make "
            "ideas sound good. Your job is to discover why they might be wrong "
            "before anyone wastes time building them."
        ),
        verbose=True,
        allow_delegation=False,
    )

    judge = Agent(
        role="Innovation Judge",
        goal=(
            "Evaluate the surviving ideas and select the strongest candidates. "
            "Prioritize originality, size of the problem, number of potential "
            "users, feasibility, defensibility, monetization potential and "
            "ability to become much larger than the initial product."
        ),
        backstory=(
            "You are the final evaluator of an innovation laboratory. "
            "You prefer ideas that solve important problems for large numbers "
            "of people while remaining realistically buildable."
        ),
        verbose=True,
        allow_delegation=False,
    )

    research_task = Task(
        description=(
            f"Study '{topic}' deeply. Identify at least 10 important signals: "
            "emerging technologies, growing problems, changing behaviors, "
            "inefficiencies, underserved users, unexpected combinations and "
            "market gaps. Distinguish observations from speculation."
        ),
        expected_output=(
            "A structured research report containing at least 10 signals, "
            "with an explanation of why each signal could matter."
        ),
        agent=researcher,
    )

    invention_task = Task(
        description=(
            "Using the research findings, generate at least 15 possible "
            "inventions, products or website/app concepts. "
            "Do not merely reproduce existing mainstream products. "
            "For every idea explain: the problem, target users, proposed "
            "solution and what makes the approach unusual."
        ),
        expected_output=(
            "A structured list of at least 15 distinct ideas with problem, "
            "solution, users and originality rationale."
        ),
        agent=inventor,
        context=[research_task],
    )

    science_task = Task(
        description=(
            "Analyze the research and proposed ideas using first-principles "
            "reasoning. Find hidden assumptions, unexpected relationships and "
            "possibilities that the other agents may have missed. Propose "
            "additional concepts when useful."
        ),
        expected_output=(
            "A rigorous analysis containing overlooked opportunities, "
            "fundamental principles and additional high-potential concepts."
        ),
        agent=scientist,
        context=[research_task, invention_task],
    )

    criticism_task = Task(
        description=(
            "Aggressively challenge the proposed ideas. For each promising "
            "concept, determine whether similar products already exist, "
            "whether the problem is genuinely painful, whether users would "
            "actually adopt it, what could make it fail and what would need "
            "to be tested first."
        ),
        expected_output=(
            "A critical evaluation of the strongest concepts, including "
            "failure modes, competition concerns and required validation."
        ),
        agent=critic,
        context=[research_task, invention_task, science_task],
    )

    judgment_task = Task(
        description=(
            "Select the 3 strongest opportunities after considering all "
            "previous work. Score each from 0 to 10 for originality, problem "
            "severity, market size, feasibility, monetization, defensibility "
            "and potential for exponential growth. Then recommend the single "
            "best opportunity and explain exactly why."
        ),
        expected_output=(
            "A ranked top-3 list with scores for every criterion, followed "
            "by one final recommendation and a concrete MVP direction."
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
    """Execute the Autonomous Discovery Lab for a given objective."""
    crew = create_autonomous_crew(topic)
    result = crew.kickoff()
    return str(result)


if __name__ == "__main__":
    print(run_crew())