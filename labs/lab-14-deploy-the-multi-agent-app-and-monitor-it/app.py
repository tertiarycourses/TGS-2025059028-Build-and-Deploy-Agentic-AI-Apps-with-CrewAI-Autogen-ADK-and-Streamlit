"""
Lab 14 — Deploy the Multi-Agent App and Monitor It

Deploy the multi-agent trip planner from Activity 6 to Streamlit Cloud, add caching and spend controls so a public multi-agent app cannot run away with your API budget, and monitor its behaviour under real use.

Deliverable: A publicly deployed multi-agent app with caching, a request cap and monitored token spend.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Deploy the multi-agent trip planner (Activity 6) to Streamlit Cloud using the Activity 12 procedure, with both OPENAI and TAVILY keys in Secrets.

    # Step 2. Note why multi-agent apps cost more: ONE user request fans out into several agent calls, each with its own tool calls.

    # Step 3. Cache the search tool results so repeated identical queries do not re-bill you.
    # @st.cache_data(ttl=3600)
    # def cached_search(query: str) -> str: ...

    # Step 4. Add a per-session request counter that stops the app after a set number of plans.
    # st.session_state.setdefault('runs', 0)
    # if st.session_state.runs >= 5: st.warning('Session limit reached'); st.stop()

    # Step 5. Set a hard monthly spend limit in the OpenAI billing dashboard — the only control that cannot be bypassed by a code bug.

    # Step 6. Run three trip plans through the public URL, then open the provider dashboard and record the tokens consumed per plan.

    # Step 7. Check the Streamlit Cloud logs for any tool errors that did not surface in the UI.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
