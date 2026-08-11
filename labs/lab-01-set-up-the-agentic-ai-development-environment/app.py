"""
Lab 1 — Set Up the Agentic AI Development Environment

Run this AFTER installing requirements.txt and creating your .env.
It verifies that every framework this course uses is importable and that
each API key is present — so you find problems now, not in Lab 12.

    python app.py
"""
import os
import importlib
from dotenv import load_dotenv

load_dotenv()

FRAMEWORKS = [
    ("streamlit", "Streamlit — the UI layer"),
    ("openai", "OpenAI Python SDK"),
    ("agents", "OpenAI Agents SDK (openai-agents)"),
    ("crewai", "CrewAI — role-based crews"),
    ("autogen_agentchat", "Microsoft AutoGen"),
    ("chromadb", "ChromaDB — vector store"),
    ("pypdf", "pypdf — PDF text extraction"),
    ("tavily", "Tavily — web search tool"),
]

KEYS = [
    ("OPENAI_API_KEY", True),
    ("TAVILY_API_KEY", True),
    ("GEMINI_API_KEY", False),
    ("OPENROUTER_API_KEY", False),
]


def check_frameworks():
    print("Frameworks")
    ok = True
    for module, label in FRAMEWORKS:
        try:
            m = importlib.import_module(module)
            version = getattr(m, "__version__", "")
            print(f"  [ok]   {label:42} {version}")
        except ImportError:
            print(f"  [MISS] {label:42} -> pip install -r requirements.txt")
            ok = False
    return ok


def check_keys():
    print("\nAPI keys (.env)")
    ok = True
    for name, required in KEYS:
        value = os.environ.get(name)
        if value:
            print(f"  [ok]   {name:22} {value[:7]}…{value[-4:]}")
        elif required:
            print(f"  [MISS] {name:22} REQUIRED — add it to .env")
            ok = False
        else:
            print(f"  [--]   {name:22} optional, not set")
    return ok


def main():
    print("=" * 62)
    print("Lab 1 — environment check")
    print("=" * 62)
    frameworks_ok = check_frameworks()
    keys_ok = check_keys()
    print("\n" + "=" * 62)
    if frameworks_ok and keys_ok:
        print("READY — every framework imports and the required keys are set.")
    else:
        print("NOT READY — fix the [MISS] lines above before the next lab.")
    print("=" * 62)


if __name__ == "__main__":
    main()
