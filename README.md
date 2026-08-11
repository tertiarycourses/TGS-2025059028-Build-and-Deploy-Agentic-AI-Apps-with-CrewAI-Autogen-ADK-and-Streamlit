# Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit

[![WSQ](https://img.shields.io/badge/WSQ-TGS--2025059028-1F6FEB)](https://www.tertiarycourses.com.sg/wsq-build-and-deploy-agentic-ai-apps-with-crewai-autogen-adk-and-streamlit.html)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![CrewAI](https://img.shields.io/badge/CrewAI-FF5A5F)](https://www.crewai.com/)
[![AutoGen](https://img.shields.io/badge/Microsoft-AutoGen-0078D4?logo=microsoft&logoColor=white)](https://microsoft.github.io/autogen/)
[![OpenAI Agents SDK](https://img.shields.io/badge/OpenAI-Agents%20SDK-412991?logo=openai&logoColor=white)](https://openai.github.io/openai-agents-python/)

Official course repository for the WSQ course **Build and Deploy Agentic AI Apps with CrewAI,
Autogen, ADK and Streamlit** (**TGS-2025059028**), delivered by
[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/) (UEN 201200696W).

**Live demo:** [Invoice RAG Chat](https://invoice-rag-openrouter.streamlit.app/)

---

## What you build

Twenty hands-on activities take you from a single tool-using agent to a publicly deployed,
guardrailed multi-agent application.

| # | Application | Framework |
|---|---|---|
| 3 | Chat agent with live web search | OpenAI Agents SDK + Tavily |
| 4 | Role-based content crew (Researcher → Writer) | CrewAI |
| 5 | Conversational writer/critic team (reflection) | Microsoft AutoGen |
| 6 | Multi-agent trip planner (agents-as-tools) | OpenAI Agents SDK |
| 8 | Invoice RAG over PDFs | ChromaDB + embeddings |
| 12 | Public cloud deployment | Streamlit Community Cloud |
| 16–17 | Input + output guardrails with tripwires | OpenAI Agents SDK guardrails |
| 20 | Guardrailed production app | everything above |

## Course structure

| Learning Unit | Focus | Activities |
|---|---|---|
| **LU1** — Agentic AI App Development | Frameworks, multi-agent workflows, workflow design, AI IDEs | 1–7 |
| **LU2** — RAG & Deployment on Streamlit Cloud | Context augmentation, knowledge graphs, cloud inference, error logs | 8–14 |
| **LU3** — Model Alignment and Guardrails | Safeguarding LLMs, alignment, deploying guardrails | 15–20 |

**Learning outcomes**

1. Design and implement multi-agent integration workflows using CrewAI, AutoGen and the OpenAI Agents SDK / ADK.
2. Develop and deploy Agentic AI and RAG applications for inference on Streamlit Cloud.
3. Deploy guardrails and model alignment techniques to ensure safe and aligned outputs.

Aligned to Skills Framework TSC **Generative AI Application Development and Deployment**
(`ICT-INT-0047-1.1`).

---

## Architecture

```
                        ┌──────────────────────────┐
   user request ───────▶│    INPUT GUARDRAIL       │  classifier agent + tripwire
                        │  injection · off-topic   │
                        └────────────┬─────────────┘
                                     │ passes
                        ┌────────────▼─────────────┐
                        │       ORCHESTRATOR       │
                        │   (agents-as-tools)      │
                        └───┬─────────┬─────────┬──┘
                   ┌────────▼──┐ ┌────▼─────┐ ┌─▼─────────┐
                   │ Planner   │ │ Budget   │ │ RAG /     │
                   │ agent     │ │ agent    │ │ retrieval │
                   └────┬──────┘ └────┬─────┘ └─────┬─────┘
                        │  tools      │             │  ChromaDB
                        └─────────────┴─────────────┘
                                     │
                        ┌────────────▼─────────────┐
                        │    OUTPUT GUARDRAIL      │  PII redaction + policy check
                        └────────────┬─────────────┘
                                     ▼
                              answer to user
                        (every decision → audit log)
```

## Repository layout

```
labs/
  app/
    simple_chat.py              Activity 3  — agent + Tavily search tool
    crew_content.py             Activity 4  — CrewAI role-based crew
    autogen_team.py             Activity 5  — AutoGen writer/critic team
    trip_planner.py             Activity 6  — multi-agent orchestrator
    trip_planner_gemini.py                  — Gemini variant
    invoice_rag.py              Activity 8  — RAG over invoice PDFs
    invoice_rag_gemini.py       Activity 11 — Gemini variant
    invoice_rag_openrouter.py   Activity 11 — OpenRouter variant
    guarded_chat.py             Activities 16, 17, 19 — guardrails + audit log
    fakes invoices/             sample PDFs for the RAG activities
  data/                         datasets for the analysis activities
  .streamlit/                   Streamlit Cloud secrets template
courseware/                     slide deck, Lesson Plan, Learner Guide (+ PDFs)
```

## Setup

```bash
git clone https://github.com/tertiarycourses/TGS-2025059028-Build-and-Deploy-Agentic-AI-Apps-with-CrewAI-Autogen-ADK-and-Streamlit.git
cd TGS-2025059028-Build-and-Deploy-Agentic-AI-Apps-with-CrewAI-Autogen-ADK-and-Streamlit

python3 -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r labs/requirements.txt
```

Create your `.env` from the template and paste in your own keys:

```bash
cp labs/app/.env.example .env
```

| Key | Where to get it | Free tier |
|---|---|---|
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com/api-keys) | pay-as-you-go |
| `TAVILY_API_KEY` | [app.tavily.com](https://app.tavily.com) | yes |
| `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com/apikey) | yes |
| `OPENROUTER_API_KEY` | [openrouter.ai](https://openrouter.ai/keys) | yes |

> **Never commit `.env`.** It is git-ignored. For Streamlit Cloud, paste the same keys into the
> app's **Secrets** manager instead (see `labs/.streamlit/secrets.toml.example`).

## Run

```bash
streamlit run labs/app/simple_chat.py        # Activity 3  — chat agent with web search
streamlit run labs/app/trip_planner.py       # Activity 6  — multi-agent trip planner
streamlit run labs/app/invoice_rag.py        # Activity 8  — invoice RAG
streamlit run labs/app/guarded_chat.py       # Activity 16 — guardrailed agent

python labs/app/crew_content.py              # Activity 4  — CrewAI crew
python labs/app/autogen_team.py              # Activity 5  — AutoGen team
```

## Deploy to Streamlit Community Cloud

1. Confirm `requirements.txt` lists every import — a missing line is the most common failure.
2. Verify no key is committed: `git grep -nE '(sk-|tvly-)[A-Za-z0-9]{20}'`
3. Push to a public GitHub repo.
4. At [share.streamlit.io](https://share.streamlit.io) → **Create app** → select the repo, branch and main file.
5. **Advanced settings → Secrets**, paste your keys in TOML format.
6. Deploy, then open the public `*.streamlit.app` URL.

## Courseware

Slides, the Lesson Plan and the Learner Guide are distributed to enrolled learners through
[lms-tms.tertiaryinfotech.com](https://lms-tms.tertiaryinfotech.com). Assessment material is
confidential and is **not** published in this repository.

## Acknowledgements

Built with [CrewAI](https://www.crewai.com/), [Microsoft AutoGen](https://microsoft.github.io/autogen/),
the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/),
[Streamlit](https://streamlit.io/), [ChromaDB](https://www.trychroma.com/) and
[Tavily](https://tavily.com/).

## License

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). All rights reserved.
Provided for the use of enrolled learners of TGS-2025059028.
