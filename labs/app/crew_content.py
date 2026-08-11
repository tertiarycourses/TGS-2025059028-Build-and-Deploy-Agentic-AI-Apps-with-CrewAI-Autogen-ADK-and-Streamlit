"""Activity 4 — Build a Role-Based Crew with CrewAI.

A two-agent content-production crew: a Researcher gathers facts and a Writer
turns them into an article. The Writer's task declares context=[research], so
CrewAI passes the Researcher's output into the Writer's prompt — this is the
handoff you should watch for in the verbose log.

Run:  python app/crew_content.py
"""
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set — add it to your .env file")

TOPIC = "Agentic AI adoption in Singapore"

# ---------------------------------------------------------------- agents
researcher = Agent(
    role="Senior Researcher",
    goal=f"Find accurate, current and specific facts about {{topic}}",
    backstory=(
        "You are a meticulous technology analyst. You prefer concrete numbers, "
        "named organisations and dated events over vague generalities, and you "
        "always say where a claim came from."
    ),
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role="Tech Content Writer",
    goal="Write a clear, engaging 400-word article on {topic}",
    backstory=(
        "You explain complex technology simply, for a business audience with no "
        "AI background. You never invent facts — you write only from the "
        "research you are given."
    ),
    verbose=True,
    allow_delegation=False,
)

# ---------------------------------------------------------------- tasks
research = Task(
    description=(
        "Research {topic}. Identify the five most important and current findings. "
        "For each, give one sentence of detail and note the kind of source it came from."
    ),
    expected_output="Exactly 5 bullet points, each with a supporting detail and a source type.",
    agent=researcher,
)

write = Task(
    description=(
        "Using ONLY the research findings provided, write a 400-word article on {topic}. "
        "Open with a hook, cover the five findings, and close with what it means for "
        "a Singapore business considering agentic AI."
    ),
    expected_output="A polished 400-word article with a title and a closing takeaway.",
    agent=writer,
    context=[research],          # <-- the handoff: Writer receives Researcher's output
)

# ---------------------------------------------------------------- crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    process=Process.sequential,  # research runs to completion, THEN write starts
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": TOPIC})
    print("\n" + "=" * 70)
    print("FINAL ARTICLE")
    print("=" * 70)
    print(result)
