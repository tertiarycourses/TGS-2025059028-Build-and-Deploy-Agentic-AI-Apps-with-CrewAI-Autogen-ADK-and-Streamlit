# Lab 11 — Swap Model Providers — Gemini and OpenRouter

**Learning outcome:** LO2 — Develop and deploy Agentic AI and RAG applications for inference on Streamlit Cloud
**Suggested duration:** 60 minutes

## Goal

Resolve real multi-model compatibility issues by pointing the same RAG application at three different providers through the OpenAI-compatible API surface: OpenAI, Google Gemini and OpenRouter. Compare cost, latency and answer quality on identical questions.

## What you'll build

The same RAG app running against three providers, with a comparison of cost, speed and answer quality.

**Tools:** OpenAI API, Gemini API, OpenRouter, labs/lab-11-swap-model-providers-gemini-and-openrouter/app.py, labs/lab-11-swap-model-providers-gemini-and-openrouter/app.py

## Workflow

1. Run the OpenAI baseline
2. Diff the Gemini variant
3. Set base_url + provider key
4. Run the OpenRouter variant
5. Compare cost / latency / quality

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Run labs/lab-08-build-a-rag-pipeline-over-invoice-pdfs/app.py once and record the answer and response time for one fixed question — your baseline.

2. Diff the Gemini variant against the OpenAI original to see exactly what a provider swap changes.

   ```bash
   diff app.py app.py
   ```

3. Note the pattern: the same OpenAI client class, redirected with base_url and a different api_key and model name.

   ```bash
   client = OpenAI(api_key=os.environ['GEMINI_API_KEY'], base_url='https://generativelanguage.googleapis.com/v1beta/openai/')
   ```

4. Get a free Gemini key at https://aistudio.google.com/apikey and add GEMINI_API_KEY to your .env.

5. Run the Gemini version and ask the same fixed question.

   ```bash
   streamlit run app.py
   ```

6. Get an OpenRouter key at https://openrouter.ai/keys, add OPENROUTER_API_KEY, and run the OpenRouter version.

   ```bash
   streamlit run app.py
   ```

7. Note the compatibility trap: embedding models are NOT interchangeable — an index built with one provider's embeddings must be rebuilt for another.

8. Record cost per 1M tokens, observed latency and answer quality for all three, and pick one for production.

## Test it

All three variants answer your fixed question correctly, and you can explain why the ChromaDB collection must be re-indexed when the embedding provider changes.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 11.
