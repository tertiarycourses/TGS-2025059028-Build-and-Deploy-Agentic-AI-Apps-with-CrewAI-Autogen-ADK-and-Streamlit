# Lab 3 — Build a Single Agent with Tools (OpenAI Agents SDK)

**Learning outcome:** LO1 — Design and implement multi-agent integration workflows using Agentic AI frameworks
**Suggested duration:** 60 minutes

## Goal

Build the course's first working agent: a Streamlit chatbot backed by the OpenAI Agents SDK that can search the live internet with a Tavily function tool. This is labs/lab-03-build-a-single-agent-with-tools-openai-agents-sdk/app.py and it introduces Agent, Runner, @function_tool and Streamlit session state.

## What you'll build

A running Streamlit chat app whose agent calls a Tavily search tool to answer questions about current events.

**Tools:** OpenAI Agents SDK, Tavily API, Streamlit, labs/lab-03-build-a-single-agent-with-tools-openai-agents-sdk/app.py

## Workflow

1. Define the @function_tool
2. Create the Agent with instructions
3. Wire Streamlit chat + session state
4. Run with Runner.run
5. Ask a current-events question

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Open labs/lab-03-build-a-single-agent-with-tools-openai-agents-sdk/app.py and read it top to bottom before running anything.

2. Find the @function_tool decorator on tavily_search — the docstring is what the model reads to decide when to call it.

3. Find the Agent(...) constructor and note its four arguments: name, model, instructions and tools.

4. Note that Runner.run(agent, input=...) is async, so the app drives it through an explicit asyncio event loop.

5. Run the app from the repository root.

   ```bash
   streamlit run app.py
   ```

6. Ask a question the model cannot know from training alone, e.g. 'What is the latest news about Singapore MRT?'

7. Change the agent's instructions to answer only in bullet points, save, and watch Streamlit hot-reload.

## Test it

The app answers a current-events question with information newer than the model's training cut-off, which proves the tavily_search tool was actually invoked rather than answered from memory.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 3.
