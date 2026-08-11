# Lab 17 — Implement Output Guardrails — PII and Content Filtering

**Learning outcome:** LO3 — Deploy guardrails and model alignment techniques to ensure safe and aligned outputs
**Suggested duration:** 60 minutes

## Goal

Screen what the agent produces before the user ever sees it. Add an output guardrail that detects and redacts personally identifiable information leaking from the invoice RAG corpus, and blocks unsafe or policy-violating content.

## What you'll build

An output guardrail that redacts PII from RAG answers and blocks policy-violating responses.

**Tools:** OpenAI Agents SDK output guardrails, Python re, labs/lab-08-build-a-rag-pipeline-over-invoice-pdfs/app.py

## Workflow

1. Identify PII in the corpus
2. Write regex redaction
3. Add an LLM policy checker
4. Wire the @output_guardrail
5. Verify PII never reaches the UI

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Ask your Activity 8 RAG app a question designed to surface personal data, e.g. 'List every customer name and address you have.'

2. Note what leaked — customer names, addresses and invoice amounts are all PII from the source documents.

3. Write regex-based redaction for the deterministic PII patterns.

   ```bash
   import re
   def redact(t):
       t = re.sub(r'[\w.+-]+@[\w-]+\.[\w.]+', '[EMAIL]', t)
       return re.sub(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b', '[CARD]', t)
   ```

4. Understand the limit of regex: it catches formats, not judgement. Add an LLM checker for context-dependent policy breaches.

   ```bash
   class OutputCheck(BaseModel):
       leaks_pii: bool
       is_unsafe: bool
   ```

5. Write the output guardrail and decorate it with @output_guardrail.

   ```bash
   @output_guardrail
   async def pii_guard(ctx, agent, output):
       r = await Runner.run(check_agent, output, context=ctx.context)
       return GuardrailFunctionOutput(output_info=r.final_output, tripwire_triggered=r.final_output.leaks_pii)
   ```

6. Attach it to the agent with output_guardrails=[pii_guard] and apply redact() to whatever is finally displayed.

7. Re-run the PII extraction question and confirm the answer is blocked or redacted.

8. Confirm legitimate business questions ('what is the total on invoice 47905?') still answer normally.

## Test it

The 'list every customer' question is now refused or fully redacted, while a specific legitimate invoice question still returns its correct answer — the filter is precise, not blunt.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 17.
