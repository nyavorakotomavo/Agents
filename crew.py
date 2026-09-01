import crewai.llms.cache as _crewai_cache

# ------------------------------------------------------------------
# Compatibilité CrewAI / LiteLLM :
# certains environnements ajoutent automatiquement cache_breakpoint.
# Groq peut refuser cette propriété.
# ------------------------------------------------------------------
_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from crewai import Agent, Crew, Process, Task

from config import get_model
from llm_factory import create_llm


def create_autonomous_crew(
    topic: str = "revolutionary technology",
) -> Crew:

    # ==============================================================
    # MODELES
    # ==============================================================
    # Les modèles et les clés viennent UNIQUEMENT de config.py.
    # Les seules variables GitHub nécessaires sont :
    #
    # G   = clé Groq researcher
    # G1  = clé Groq inventor
    # G2  = clé Groq scientist
    # OP  = clé OpenRouter critic
    # OP2 = clé OpenRouter judge
    # OP3 = clé OpenRouter strategist
    # GEM = clé Gemini
    # ==============================================================

    researcher_model = get_model("researcher")
    inventor_model = get_model("inventor")
    scientist_model = get_model("scientist")
    critic_model = get_model("critic")
    judge_model = get_model("judge")

    # ==============================================================
    # AGENT 1 — GLOBAL RESEARCHER
    # ==============================================================

    researcher = Agent(
        role="Global Researcher",

        goal=(
            f"Investigate the world around '{topic}'. Identify emerging "
            "technologies, important problems, changing behaviors, market "
            "gaps, underserved users and overlooked opportunities. "
            "Prioritize signals that could lead to scalable products."
        ),

        backstory=(
            "You are a multidisciplinary global researcher. You investigate "
            "technology, science, economics, society and human behavior. "
            "You search for weak signals, emerging patterns and connections "
            "that ordinary analysis misses."
        ),

        llm=create_llm(researcher_model),

        verbose=True,
        allow_delegation=False,
    )

    # ==============================================================
    # AGENT 2 — RADICAL INVENTOR
    # ==============================================================

    inventor = Agent(
        role="Radical Inventor",

        goal=(
            f"Create original and potentially transformative solutions "
            f"related to '{topic}'. Combine distant fields, technologies "
            "and human needs. Avoid generic startup ideas."
        ),

        backstory=(
            "You are an unconventional inventor. You deliberately explore "
            "unexpected combinations of technologies, business models and "
            "human needs. You value originality but remain aware of what "
            "a small team could realistically build."
        ),

        llm=create_llm(inventor_model),

        verbose=True,
        allow_delegation=False,
    )

    # ==============================================================
    # AGENT 3 — SCIENTIFIC THINKER
    # ==============================================================

    scientist = Agent(
        role="Scientific Thinker",

        goal=(
            f"Analyze '{topic}' using first-principles reasoning. "
            "Identify fundamental mechanisms, hidden assumptions, "
            "technical possibilities and unexpected opportunities."
        ),

        backstory=(
            "You are a rigorous scientific thinker. You use first "
            "principles, abstraction, causal reasoning and thought "
            "experiments to determine what is actually possible."
        ),

        llm=create_llm(scientist_model),

        verbose=True,
        allow_delegation=False,
    )

    # ==============================================================
    # AGENT 4 — ADVERSARIAL CRITIC
    # ==============================================================

    critic = Agent(
        role="Adversarial Critic",

        goal=(
            "Attack the proposed ideas. Identify competitors, technical "
            "obstacles, adoption barriers, weak assumptions, economic "
            "problems, regulatory risks and reasons each idea could fail."
        ),

        backstory=(
            "You are an aggressive but constructive skeptic. Your job is "
            "to destroy weak ideas before the team wastes resources. "
            "You distinguish genuine weaknesses from solvable problems."
        ),

        llm=create_llm(critic_model),

        verbose=True,
        allow_delegation=False,
    )

    # ==============================================================
    # AGENT 5 — INNOVATION JUDGE
    # ==============================================================

    judge = Agent(
        role="Innovation Judge",

        goal=(
            "Evaluate the strongest ideas according to originality, "
            "problem severity, market size, feasibility for a small team, "
            "monetization, defensibility, scalability and growth potential."
        ),

        backstory=(
            "You are the final innovation evaluator. You compare ideas "
            "objectively and prefer opportunities capable of producing "
            "large real-world impact while remaining realistically "
            "implementable."
        ),

        llm=create_llm(judge_model),

        verbose=True,
        allow_delegation=False,
    )

    # ==============================================================
    # TASK 1 — RESEARCH
    # ==============================================================

    research_task = Task(
        description=(
            f"Investigate '{topic}'. Identify at least 10 meaningful "
            "signals, problems, trends, inefficiencies or opportunities.\n\n"
            "For each signal provide:\n"
            "1. The observed problem or trend.\n"
            "2. Who is affected.\n"
            "3. Why it matters.\n"
            "4. Why current solutions are insufficient.\n"
            "5. Potential opportunity for a new product."
        ),

        expected_output=(
            "A structured research report containing at least 10 strong "
            "signals, with evidence-based reasoning and a clear explanation "
            "of the opportunity represented by each signal."
        ),

        agent=researcher,
    )

    # ==============================================================
    # TASK 2 — INVENTION
    # ==============================================================

    invention_task = Task(
        description=(
            "Using the research produced by the Global Researcher, "
            "generate at least 15 genuinely distinct product concepts.\n\n"
            "For every concept describe:\n"
            "1. The problem.\n"
            "2. Target users.\n"
            "3. Proposed solution.\n"
            "4. Why existing solutions are insufficient.\n"
            "5. What makes the idea unusual.\n"
            "6. How a small team could build an MVP.\n"
            "7. Potential scalability."
        ),

        expected_output=(
            "At least 15 structured and clearly differentiated product "
            "concepts. Avoid superficial variations of the same idea."
        ),

        agent=inventor,

        context=[
            research_task,
        ],
    )

    # ==============================================================
    # TASK 3 — SCIENCE
    # ==============================================================

    science_task = Task(
        description=(
            "Analyze the research and proposed ideas using "
            "first-principles reasoning.\n\n"
            "Determine:\n"
            "- which assumptions are valid;\n"
            "- which assumptions are questionable;\n"
            "- what technical mechanisms could make the ideas work;\n"
            "- what hidden opportunities exist;\n"
            "- which ideas deserve deeper investigation.\n\n"
            "Propose additional concepts when the analysis reveals "
            "important opportunities."
        ),

        expected_output=(
            "A rigorous technical and conceptual analysis identifying "
            "the strongest mechanisms, hidden opportunities and the ideas "
            "that deserve further development."
        ),

        agent=scientist,

        context=[
            research_task,
            invention_task,
        ],
    )

    # ==============================================================
    # TASK 4 — CRITICISM
    # ==============================================================

    criticism_task = Task(
        description=(
            "Aggressively challenge the proposed ideas.\n\n"
            "For the strongest concepts examine:\n"
            "- competition;\n"
            "- technical feasibility;\n"
            "- user demand;\n"
            "- adoption difficulty;\n"
            "- economics;\n"
            "- monetization;\n"
            "- scalability;\n"
            "- defensibility;\n"
            "- failure modes;\n"
            "- major risks.\n\n"
            "Do not reject an idea merely because it has risks. "
            "Identify whether each weakness is fatal, serious or solvable."
        ),

        expected_output=(
            "A detailed adversarial evaluation of the strongest concepts, "
            "with risks classified as fatal, serious or solvable."
        ),

        agent=critic,

        context=[
            research_task,
            invention_task,
            science_task,
        ],
    )

    # ==============================================================
    # TASK 5 — FINAL JUDGMENT
    # ==============================================================

    judgment_task = Task(
        description=(
            "Select the three strongest opportunities from the complete "
            "analysis.\n\n"
            "Score each idea from 0 to 10 for:\n"
            "- originality;\n"
            "- problem severity;\n"
            "- market size;\n"
            "- feasibility;\n"
            "- monetization;\n"
            "- defensibility;\n"
            "- scalability;\n"
            "- growth potential.\n\n"
            "Calculate an overall assessment, rank the three ideas, "
            "choose one final winner and design a realistic MVP for it."
        ),

        expected_output=(
            "A ranked top-three list with scores and reasoning, followed "
            "by one final winning concept and a concrete MVP plan."
        ),

        agent=judge,

        context=[
            research_task,
            invention_task,
            science_task,
            criticism_task,
        ],
    )

    # ==============================================================
    # CREW
    # ==============================================================

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


# ==============================================================
# EXECUTION
# ==============================================================

def run_crew(
    topic: str = "revolutionary technology",
) -> str:

    crew = create_autonomous_crew(topic)

    result = crew.kickoff()

    return str(result)


if __name__ == "__main__":
    print(run_crew())