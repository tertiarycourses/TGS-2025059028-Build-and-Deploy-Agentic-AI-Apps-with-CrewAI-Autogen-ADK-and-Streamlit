# Lab 4 — Build a Role-Based Crew with CrewAI

**Learning outcome:** LO1 — Design and implement multi-agent integration workflows using Agentic AI frameworks
**Suggested duration:** 60 minutes

## Goal

Model a content-production team as a CrewAI crew: a Researcher agent gathers facts and a Writer agent turns them into an article. Each agent gets a role, goal and backstory, and the tasks run in a sequential process where task 2 consumes task 1's output.

## What you'll build

A Python script that runs a two-agent CrewAI crew and prints a finished article on a topic you choose.

**Tools:** CrewAI, OpenAI API, labs/lab-04-build-a-role-based-crew-with-crewai/app.py

## Workflow

1. Define Researcher + Writer agents
2. Write the two Tasks
3. Assemble the Crew (sequential)
4. crew.kickoff() with inputs
5. Read the handed-off output

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Create labs/lab-04-build-a-role-based-crew-with-crewai/app.py and import Agent, Task, Crew and Process from crewai.

   ```bash
   from crewai import Agent, Task, Crew, Process
   ```

2. Define the Researcher agent with a role, a goal and a backstory — the backstory steers its tone and depth.

   ```bash
   researcher = Agent(role='Senior Researcher', goal='Find accurate, current facts about {topic}', backstory='You are a meticulous analyst who cites sources.', verbose=True)
   ```

3. Define the Writer agent the same way, giving it the job of turning research notes into prose.

   ```bash
   writer = Agent(role='Tech Content Writer', goal='Write a clear 400-word article on {topic}', backstory='You explain complex topics simply.', verbose=True)
   ```

4. Create the research Task with a description and an expected_output — expected_output is what makes the result predictable.

   ```bash
   research = Task(description='Research {topic} and list 5 key findings.', expected_output='5 bullet points with sources.', agent=researcher)
   ```

5. Create the writing Task and pass context=[research] so it receives the researcher's output.

   ```bash
   write = Task(description='Write the article using the research.', expected_output='A 400-word article.', agent=writer, context=[research])
   ```

6. Assemble the Crew with both agents, both tasks and Process.sequential, then kick it off with a topic.

   ```bash
   crew = Crew(agents=[researcher, writer], tasks=[research, write], process=Process.sequential)
   print(crew.kickoff(inputs={'topic': 'Agentic AI in Singapore'}))
   ```

7. Run the script and watch the verbose log show the handoff from Researcher to Writer.

   ```bash
   python app.py
   ```

## Test it

The verbose output shows the Researcher task completing FIRST and the Writer task quoting its findings — proving context was passed between agents rather than each working in isolation.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 4.
