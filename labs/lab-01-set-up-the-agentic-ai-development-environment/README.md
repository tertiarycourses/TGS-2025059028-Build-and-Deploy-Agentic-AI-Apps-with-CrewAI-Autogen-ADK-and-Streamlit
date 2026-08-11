# Lab 1 — Set Up the Agentic AI Development Environment

**Learning outcome:** LO1 — Design and implement multi-agent integration workflows using Agentic AI frameworks
**Suggested duration:** 45 minutes

## Goal

Prepare the Python environment every later activity depends on: a virtual environment, the agent frameworks, and the API keys for OpenAI, Tavily and OpenRouter stored safely in a .env file that is never committed to source control.

## What you'll build

A working .venv with CrewAI, AutoGen, the OpenAI Agents SDK and Streamlit installed, plus a .env holding your API keys.

**Tools:** Python 3.11+, pip, venv, VS Code, OpenAI Platform, Tavily, OpenRouter

## Workflow

1. Create and activate .venv
2. pip install the frameworks
3. Get OpenAI + Tavily API keys
4. Save keys into .env
5. Verify with a version check

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Clone the course repository and change into it.

   ```bash
   git clone https://github.com/tertiarycourses/TGS-2025059028-Build-and-Deploy-Agentic-AI-Apps-with-CrewAI-Autogen-ADK-and-Streamlit.git && cd TGS-2025059028-*
   ```

2. Create a Python virtual environment and activate it (use .venv\Scripts\activate on Windows).

   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```

3. Install the agent frameworks and the app dependencies used by every activity.

   ```bash
   pip install streamlit openai openai-agents crewai autogen-agentchat autogen-ext[openai] python-dotenv pypdf chromadb tavily-python
   ```

4. Create an API key at https://platform.openai.com/api-keys and a free search key at https://app.tavily.com — copy both.

5. Create a .env file in the project root and paste your keys into it, one per line.

   ```bash
   printf 'OPENAI_API_KEY=sk-...\nTAVILY_API_KEY=tvly-...\nOPENROUTER_API_KEY=sk-or-...\n' > .env
   ```

6. Confirm .env is listed in .gitignore so your keys are never pushed to GitHub.

   ```bash
   grep -n '.env' .gitignore || echo '.env' >> .gitignore
   ```

7. Verify the installation by printing the installed framework versions.

   ```bash
   python -c "import crewai, agents, streamlit; print(crewai.__version__, streamlit.__version__)"
   ```

## Test it

The version command prints without an ImportError, `pip list` shows crewai, openai-agents, autogen-agentchat and streamlit, and `git status` does NOT list .env as a file to be committed.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 1.
