# Lab 6 — Orchestrate a Multi-Agent Trip Planner (Agents-as-Tools)

**Learning outcome:** LO1 — Design and implement multi-agent integration workflows using Agentic AI frameworks
**Suggested duration:** 75 minutes

## Goal

Build the course's flagship multi-agent app: a Streamlit trip planner where an orchestrator delegates to Planner, Budget and Local Guide agents exposed via the .as_tool() pattern, each with its own Tavily search tool and Pydantic-structured output. This is labs/lab-06-orchestrate-a-multi-agent-trip-planner-agents-as-tools/app.py.

## What you'll build

A Streamlit app that produces a day-by-day itinerary, a budget breakdown and local food tips from three specialist agents.

**Tools:** OpenAI Agents SDK, Tavily API, Pydantic, Streamlit, labs/lab-06-orchestrate-a-multi-agent-trip-planner-agents-as-tools/app.py

## Workflow

1. Review the 3 specialist agents
2. See .as_tool() delegation
3. Note the Pydantic output models
4. Run the Streamlit app
5. Plan a real trip and read the tabs

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Open labs/lab-06-orchestrate-a-multi-agent-trip-planner-agents-as-tools/app.py and locate the four Tavily @function_tool definitions at the top.

2. Find the three specialist agents — Planner, Budget and Local Guide — and note each one gets only the search tools it needs.

3. Find the Pydantic BaseModel classes: structured output is what lets the UI render clean tabs instead of raw text.

4. Find the orchestrator agent and the .as_tool(...) calls that turn each specialist agent INTO a callable tool.

5. Understand the key idea: the orchestrator does not hard-code the order — the model decides which specialist to invoke and when.

6. Run the app and enter a real trip: destination, number of days and a budget.

   ```bash
   streamlit run app.py
   ```

7. Read each result tab and confirm the itinerary, the costs and the food tips are consistent with each other.

8. Add a fourth specialist (e.g. a Weather agent), expose it with .as_tool(), and register it on the orchestrator.

## Test it

The app returns all three sections populated for a real destination, and the terminal shows the orchestrator calling more than one specialist tool for a single user request.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 6.
