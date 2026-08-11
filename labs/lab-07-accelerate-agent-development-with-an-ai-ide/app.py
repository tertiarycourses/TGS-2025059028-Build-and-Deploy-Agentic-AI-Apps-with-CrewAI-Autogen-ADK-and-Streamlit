"""
Lab 7 — Accelerate Agent Development with an AI IDE

Use an AI IDE — GitHub Copilot, Cursor, Trae or Windsurf — to extend an existing agent. Generate a new function tool from a comment, use the chat panel to explain unfamiliar agent code, and let the IDE diagnose a deliberately broken tool definition.

Deliverable: A new, working function tool added to simple_chat.py that was drafted by the AI IDE and verified by you.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Install your AI IDE — GitHub Copilot in VS Code, or download Cursor / Trae / Windsurf.

    # Step 2. Open this lab's app.py (copied from Lab 3), select the whole file, and ask the chat panel: 'Explain how this agent decides to call a tool.'

    # Step 3. At the end of the tool section, type a comment describing a new tool, then let the IDE complete it.
    # # @function_tool that returns today's date and the current time in Singapore

    # Step 4. Review the generated code critically — check the decorator, the type hints and especially the docstring.

    # Step 5. Fix anything the IDE got wrong. The docstring matters most: it is the only thing the model sees when choosing a tool.

    # Step 6. Register the new tool in the Agent's tools list.
    # tools=[tavily_search, get_singapore_time],

    # Step 7. Run the app and ask 'What time is it in Singapore right now?' to confirm the new tool is selected.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
