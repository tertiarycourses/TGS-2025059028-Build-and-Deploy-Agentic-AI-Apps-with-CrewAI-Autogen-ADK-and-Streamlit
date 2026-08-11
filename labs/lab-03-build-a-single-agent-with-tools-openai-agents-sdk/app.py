"""
Lab 3 — Build a Single Agent with Tools (OpenAI Agents SDK)

A Streamlit chatbot backed by the OpenAI Agents SDK that can search the live
internet with a Tavily function tool. This is the smallest complete agent:
an LLM + instructions + one tool + conversation state.

    streamlit run app.py
"""
import asyncio
import os

import streamlit as st
from dotenv import load_dotenv
from tavily import TavilyClient

from agents import Agent, Runner, function_tool

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
tavily_key = os.environ.get("TAVILY_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set — add it to your .env file")
if not tavily_key:
    raise ValueError("TAVILY_API_KEY is not set — add it to your .env file")


@function_tool
def tavily_search(query: str) -> str:
    """Search the internet for current information.

    Use this whenever the question concerns recent events, live prices, news,
    or anything that may have changed after your training cut-off.
    """
    tavily = TavilyClient(api_key=tavily_key)
    response = tavily.search(query=query, search_depth="basic")
    results = response.get("results", [])
    return "\n".join(
        f"Source: {r['url']}\nContent: {r['content']}" for r in results
    ) or "No results found."


agent = Agent(
    name="Chat Assistant",
    model="gpt-4.1-mini",
    instructions=(
        "You are a helpful and friendly assistant. Respond concisely. "
        "Use the tavily_search tool to look up current information when needed."
    ),
    tools=[tavily_search],
)

st.set_page_config(page_title="Lab 3 — Agent with Tools", page_icon="🤖")
st.title("🤖 A Simple Chatbot Agent")
st.caption("OpenAI Agents SDK + Tavily search — Lab 3")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask me anything — try a current-events question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"), st.spinner("Thinking…"):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(
            Runner.run(agent, input=st.session_state.messages)
        )
        st.write(result.final_output)

    st.session_state.messages.append(
        {"role": "assistant", "content": result.final_output}
    )

if st.button("New Chat"):
    st.session_state.messages = []
    st.rerun()
