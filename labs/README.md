# Labs — Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit

**WSQ Course Code:** TGS-2025059028  |  **Tertiary Infotech Academy Pte Ltd**

20 hands-on labs, one folder each. Every folder is self-contained: a README with the full steps, the app code, and its own requirements.txt.

## Before you start

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
cp .env.example .env            # then paste in your own API keys
```

Never commit `.env`. For Streamlit Cloud, paste the same keys into the app's Secrets manager instead — see `.streamlit/secrets.toml.example`.

## Learning Unit 01 — Agentic AI App Development with Agentic AI Frameworks

| Lab | Title | Build | Minutes |
|----|-------|-------|---------|
| 1 | [Set Up the Agentic AI Development Environment](./lab-01-set-up-the-agentic-ai-development-environment/) | A working .venv with CrewAI, AutoGen, the OpenAI Agents SDK and Streamlit inst… | 45 |
| 2 | [Compare CrewAI, AutoGen and the OpenAI Agents SDK](./lab-02-compare-crewai-autogen-and-the-openai-agents-sdk/) | A completed framework-comparison matrix with a written, evidence-based recomme… | 30 |
| 3 | [Build a Single Agent with Tools (OpenAI Agents SDK)](./lab-03-build-a-single-agent-with-tools-openai-agents-sdk/) | A running Streamlit chat app whose agent calls a Tavily search tool to answer … | 60 |
| 4 | [Build a Role-Based Crew with CrewAI](./lab-04-build-a-role-based-crew-with-crewai/) | A Python script that runs a two-agent CrewAI crew and prints a finished articl… | 60 |
| 5 | [Build a Conversational Team with AutoGen](./lab-05-build-a-conversational-team-with-autogen/) | An AutoGen round-robin team where an assistant and a critic iterate on a task … | 60 |
| 6 | [Orchestrate a Multi-Agent Trip Planner (Agents-as-Tools)](./lab-06-orchestrate-a-multi-agent-trip-planner-agents-as-tools/) | A Streamlit app that produces a day-by-day itinerary, a budget breakdown and l… | 75 |
| 7 | [Accelerate Agent Development with an AI IDE](./lab-07-accelerate-agent-development-with-an-ai-ide/) | A new, working function tool added to simple_chat.py that was drafted by the A… | 45 |

## Learning Unit 02 — Agentic AI and RAG Deployment on Streamlit Cloud

| Lab | Title | Build | Minutes |
|----|-------|-------|---------|
| 8 | [Build a RAG Pipeline over Invoice PDFs](./lab-08-build-a-rag-pipeline-over-invoice-pdfs/) | A Streamlit app that indexes the sample invoice PDFs and answers questions abo… | 75 |
| 9 | [Tune Retrieval Quality — Chunking and Top-K](./lab-09-tune-retrieval-quality-chunking-and-top-k/) | A completed retrieval-tuning table showing accuracy at three chunk sizes and t… | 45 |
| 10 | [Context Augmentation with a Knowledge Graph](./lab-10-context-augmentation-with-a-knowledge-graph/) | A small invoice knowledge graph (customer → invoice → line item) and a multi-h… | 45 |
| 11 | [Swap Model Providers — Gemini and OpenRouter](./lab-11-swap-model-providers-gemini-and-openrouter/) | The same RAG app running against three providers, with a comparison of cost, s… | 60 |
| 12 | [Deploy a RAG App to Streamlit Cloud](./lab-12-deploy-a-rag-app-to-streamlit-cloud/) | A publicly reachable Streamlit Cloud URL running YOUR RAG app, with secrets co… | 75 |
| 13 | [Diagnose Deployment Failures from Error Logs](./lab-13-diagnose-deployment-failures-from-error-logs/) | A completed error-log triage table mapping four real log signatures to their r… | 45 |
| 14 | [Deploy the Multi-Agent App and Monitor It](./lab-14-deploy-the-multi-agent-app-and-monitor-it/) | A publicly deployed multi-agent app with caching, a request cap and monitored … | 60 |

## Learning Unit 03 — Model Alignment and Guardrails

| Lab | Title | Build | Minutes |
|----|-------|-------|---------|
| 15 | [Attack Your Own Agent — Red-Team the Baseline](./lab-15-attack-your-own-agent-red-team-the-baseline/) | A completed red-team log of attacks attempted, which succeeded, and the guardr… | 45 |
| 16 | [Implement Input Guardrails with Tripwires](./lab-16-implement-input-guardrails-with-tripwires/) | An input guardrail that blocks the injection and off-topic attacks you logged … | 60 |
| 17 | [Implement Output Guardrails — PII and Content Filtering](./lab-17-implement-output-guardrails-pii-and-content-filtering/) | An output guardrail that redacts PII from RAG answers and blocks policy-violat… | 60 |
| 18 | [Evaluate Model Alignment — Helpful, Harmless, Honest](./lab-18-evaluate-model-alignment-helpful-harmless-honest/) | A scored alignment evaluation across ten prompts, with the helpful/harmless/ho… | 45 |
| 19 | [Add Human Oversight and an Audit Log](./lab-19-add-human-oversight-and-an-audit-log/) | An agent with a human-approval gate on high-risk actions and a persistent JSON… | 45 |
| 20 | [Deploy the Guardrailed Agentic AI App to Production](./lab-20-deploy-the-guardrailed-agentic-ai-app-to-production/) | A publicly deployed, fully guardrailed Agentic AI application that passes a li… | 75 |

## Running a lab

```bash
cd lab-03-build-a-single-agent-with-tools-openai-agents-sdk
pip install -r requirements.txt
streamlit run app.py            # or: python app.py
```

---

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). Provided for the use of enrolled learners.
