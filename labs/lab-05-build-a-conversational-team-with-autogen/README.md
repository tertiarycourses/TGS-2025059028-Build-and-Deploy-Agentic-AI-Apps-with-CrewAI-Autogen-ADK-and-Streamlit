# Lab 5 — Build a Conversational Team with AutoGen

**Learning outcome:** LO1 — Design and implement multi-agent integration workflows using Agentic AI frameworks
**Suggested duration:** 60 minutes

## Goal

Use Microsoft AutoGen to solve a problem through a structured conversation between two agents. A primary assistant proposes a solution and a critic reviews it, looping until the critic approves — the reflection pattern implemented as agent dialogue.

## What you'll build

An AutoGen round-robin team where an assistant and a critic iterate on a task until a termination condition fires.

**Tools:** AutoGen AgentChat, OpenAI API, labs/lab-05-build-a-conversational-team-with-autogen/app.py

## Workflow

1. Create the model client
2. Define assistant + critic agents
3. Set the termination condition
4. RoundRobinGroupChat.run_stream
5. Watch the critique loop

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Create labs/lab-05-build-a-conversational-team-with-autogen/app.py and import the AgentChat classes.

   ```bash
   from autogen_agentchat.agents import AssistantAgent
   from autogen_agentchat.teams import RoundRobinGroupChat
   from autogen_agentchat.conditions import TextMentionTermination
   from autogen_ext.models.openai import OpenAIChatCompletionClient
   ```

2. Create the shared model client that both agents will use.

   ```bash
   model_client = OpenAIChatCompletionClient(model='gpt-4.1-mini')
   ```

3. Define the primary assistant that does the work.

   ```bash
   primary = AssistantAgent('writer', model_client=model_client, system_message='You write short marketing copy.')
   ```

4. Define the critic and tell it the exact word to say when satisfied — this is what stops the loop.

   ```bash
   critic = AssistantAgent('critic', model_client=model_client, system_message='Give specific feedback. Reply APPROVE only when the copy is excellent.')
   ```

5. Create the termination condition and the round-robin team.

   ```bash
   team = RoundRobinGroupChat([primary, critic], termination_condition=TextMentionTermination('APPROVE'))
   ```

6. Run the team asynchronously on a task and stream the conversation to the console.

   ```bash
   import asyncio
   from autogen_agentchat.ui import Console
   asyncio.run(Console(team.run_stream(task='Write a tagline for a WSQ agentic AI course.')))
   ```

7. Read the transcript: note how the critic's feedback changes the assistant's next attempt.

   ```bash
   python app.py
   ```

## Test it

The console transcript shows at least two rounds — an initial draft, a specific critique, and a revised draft — and the conversation stops as soon as the critic emits APPROVE.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 5.
