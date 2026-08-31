# 🤖 Autonomous Agents

An autonomous multi-agent laboratory designed to investigate objectives,
discover opportunities, generate hypotheses, challenge ideas and select
the most promising solutions.

## 🧠 Current architecture

The system currently contains five cognitive roles:

- 🔭 Global Researcher
- 💡 Radical Inventor
- 🔬 Scientific Thinker
- ⚔️ Adversarial Critic
- 🏆 Innovation Judge

The agents work sequentially:

Research → Invention → Scientific Analysis → Criticism → Evaluation

## 🎯 Current objective

The first mission is to discover potentially revolutionary website or
application ideas with:

- a real and important problem;
- a large potential audience;
- global potential;
- strong differentiation;
- realistic MVP feasibility;
- monetization potential;
- long-term growth potential.

## 🚀 Execution

The project can be executed through:

1. GitHub Actions
2. The FastAPI interface

GitHub Actions can receive an objective and execute the discovery crew
automatically.

## 🔐 Secrets

API keys must NEVER be committed to this repository.

Expected GitHub Actions secrets:

- `OPENAI_API_KEY`
- `GEMINI_API_KEY`

Optional repository variable:

- `MODEL`

## 🛠️ Roadmap

### Phase 1 — Foundation
- [x] CrewAI
- [x] Multi-agent architecture
- [x] FastAPI interface
- [x] GitHub Actions workflow
- [x] Result artifacts

### Phase 2 — Intelligence
- [ ] Real web research
- [ ] Source extraction
- [ ] Persistent memory
- [ ] Better evaluation
- [ ] Iterative reasoning

### Phase 3 — Autonomy
- [ ] Dynamic task planning
- [ ] Autonomous loops
- [ ] Automatic objective decomposition
- [ ] Automatic tool selection
- [ ] Scheduled missions

### Phase 4 — Discovery Laboratory
- [ ] Long-term memory
- [ ] Idea evolution
- [ ] Experimentation
- [ ] Hypothesis testing
- [ ] Opportunity monitoring
- [ ] Automatic reports

## ⚠️ Philosophy

The system should not simply generate plausible text.

Its long-term goal is to:

**observe → investigate → hypothesize → challenge → test → learn → improve**

Originality is not assumed. Ideas must be investigated and challenged
before being considered valuable.