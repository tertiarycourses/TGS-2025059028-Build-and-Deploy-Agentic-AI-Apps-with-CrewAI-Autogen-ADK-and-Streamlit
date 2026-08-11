# Lab 7 — Accelerate Agent Development with an AI IDE

**Learning outcome:** LO1 — Design and implement multi-agent integration workflows using Agentic AI frameworks
**Suggested duration:** 45 minutes

## Goal

Use an AI IDE — GitHub Copilot, Cursor, Trae or Windsurf — to extend an existing agent. Generate a new function tool from a comment, use the chat panel to explain unfamiliar agent code, and let the IDE diagnose a deliberately broken tool definition.

## What you'll build

A new, working function tool added to simple_chat.py that was drafted by the AI IDE and verified by you.

**Tools:** GitHub Copilot / Cursor / Trae / Windsurf, VS Code, labs/lab-03-build-a-single-agent-with-tools-openai-agents-sdk/app.py

## Workflow

1. Install and sign in to the AI IDE
2. Ask chat to explain the agent code
3. Comment-driven tool generation
4. Review and correct the draft
5. Run and confirm the tool fires

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Install your AI IDE — GitHub Copilot in VS Code, or download Cursor / Trae / Windsurf.

2. Open this lab's app.py (copied from Lab 3), select the whole file, and ask the chat panel: 'Explain how this agent decides to call a tool.'

3. At the end of the tool section, type a comment describing a new tool, then let the IDE complete it.

   ```bash
   # @function_tool that returns today's date and the current time in Singapore
   ```

4. Review the generated code critically — check the decorator, the type hints and especially the docstring.

5. Fix anything the IDE got wrong. The docstring matters most: it is the only thing the model sees when choosing a tool.

6. Register the new tool in the Agent's tools list.

   ```bash
   tools=[tavily_search, get_singapore_time],
   ```

7. Run the app and ask 'What time is it in Singapore right now?' to confirm the new tool is selected.

   ```bash
   streamlit run app.py
   ```

## Test it

The agent answers the time question by calling YOUR new tool (not by guessing), and you can state one specific thing the AI IDE generated incorrectly that you had to fix — AI-assisted, human-verified.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 7.
