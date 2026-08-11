"""
Lab 5 — Build a Conversational Team with AutoGen

A round-robin team of two agents implementing the reflection pattern: a writer
proposes copy, a critic reviews it, and the loop repeats until the critic emits
the exact termination word APPROVE.

Watch the transcript: the critic's specific feedback should visibly change the
writer's next draft. That is reflection working.

    python app.py
"""
import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import (MaxMessageTermination,
                                          TextMentionTermination)
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set — add it to your .env file")

TASK = ("Write a one-line tagline for a WSQ course on building and deploying "
        "agentic AI apps.")


async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1-mini")

    writer = AssistantAgent(
        name="writer",
        model_client=model_client,
        system_message=(
            "You write short, punchy marketing copy. When you receive feedback, "
            "produce a revised version that addresses every point raised."
        ),
    )

    critic = AssistantAgent(
        name="critic",
        model_client=model_client,
        system_message=(
            "You are a demanding copy critic. Give specific, actionable "
            "feedback — say what is weak and why. Reply with the single word "
            "APPROVE only when the copy is genuinely excellent."
        ),
    )

    # Stop on APPROVE, with a hard message cap so the loop can never run away.
    termination = TextMentionTermination("APPROVE") | MaxMessageTermination(10)

    team = RoundRobinGroupChat([writer, critic], termination_condition=termination)

    await Console(team.run_stream(task=TASK))
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
