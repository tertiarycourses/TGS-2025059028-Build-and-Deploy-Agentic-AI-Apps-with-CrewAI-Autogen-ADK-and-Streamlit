# Lab 14 — Deploy the Multi-Agent App and Monitor It

**Learning outcome:** LO2 — Develop and deploy Agentic AI and RAG applications for inference on Streamlit Cloud
**Suggested duration:** 60 minutes

## Goal

Deploy the multi-agent trip planner from Activity 6 to Streamlit Cloud, add caching and spend controls so a public multi-agent app cannot run away with your API budget, and monitor its behaviour under real use.

## What you'll build

A publicly deployed multi-agent app with caching, a request cap and monitored token spend.

**Tools:** Streamlit Community Cloud, OpenAI usage dashboard, st.cache_data, labs/lab-06-orchestrate-a-multi-agent-trip-planner-agents-as-tools/app.py

## Workflow

1. Deploy trip_planner.py
2. Add st.cache_data to searches
3. Cap requests per session
4. Set a provider spend limit
5. Monitor logs and token usage

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Deploy the multi-agent trip planner (Activity 6) to Streamlit Cloud using the Activity 12 procedure, with both OPENAI and TAVILY keys in Secrets.

2. Note why multi-agent apps cost more: ONE user request fans out into several agent calls, each with its own tool calls.

3. Cache the search tool results so repeated identical queries do not re-bill you.

   ```bash
   @st.cache_data(ttl=3600)
   def cached_search(query: str) -> str: ...
   ```

4. Add a per-session request counter that stops the app after a set number of plans.

   ```bash
   st.session_state.setdefault('runs', 0)
   if st.session_state.runs >= 5: st.warning('Session limit reached'); st.stop()
   ```

5. Set a hard monthly spend limit in the OpenAI billing dashboard — the only control that cannot be bypassed by a code bug.

6. Run three trip plans through the public URL, then open the provider dashboard and record the tokens consumed per plan.

7. Check the Streamlit Cloud logs for any tool errors that did not surface in the UI.

## Test it

The deployed app serves a trip plan from its public URL, a repeated identical search returns noticeably faster (cache hit), and you can state the measured token cost of a single trip plan.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 14.
