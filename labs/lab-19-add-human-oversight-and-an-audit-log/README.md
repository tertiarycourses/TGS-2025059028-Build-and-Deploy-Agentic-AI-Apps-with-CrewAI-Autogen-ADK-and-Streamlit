# Lab 19 — Add Human Oversight and an Audit Log

**Learning outcome:** LO3 — Deploy guardrails and model alignment techniques to ensure safe and aligned outputs
**Suggested duration:** 45 minutes

## Goal

Automated guardrails cannot judge every case. Add a risk-based approval gate that routes high-impact or low-confidence actions to a human before execution, and write an audit log that records every guardrail decision for later review.

## What you'll build

An agent with a human-approval gate on high-risk actions and a persistent JSONL audit log of every decision.

**Tools:** Streamlit, Python logging, labs/lab-19-add-human-oversight-and-an-audit-log/app.py (the audit log is created when you run this step)

## Workflow

1. Classify actions by risk
2. Auto-approve low risk
3. Gate high risk on a human click
4. Log every decision to JSONL
5. Review the audit trail

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. List the actions your agent can take and classify each as low, medium or high risk.

2. Set the policy: low risk executes automatically, medium risk is logged, high risk requires explicit human approval.

3. Implement the approval gate in Streamlit for high-risk actions.

   ```bash
   if risk == 'high':
       st.warning(f'Approval required: {action}')
       if not st.button('Approve'): st.stop()
   ```

4. Write every guardrail decision to an append-only audit log as one JSON object per line.

   ```bash
   import json, datetime
   with open('data/audit_log.jsonl','a') as f:
       f.write(json.dumps({'ts': datetime.datetime.now().isoformat(), 'prompt': p, 'decision': d, 'risk': risk}) + '\n')
   ```

5. Include in each record what was requested, what the guardrail decided, the risk level and who approved it.

6. Run a mixed session: several benign requests and two high-risk ones, approving one and rejecting the other.

7. Read back the audit log and confirm you can reconstruct exactly what happened and why.

   ```bash
   cat data/audit_log.jsonl | python -m json.tool --json-lines
   ```

## Test it

A high-risk action does NOT execute until you click Approve, and the audit log lets you reconstruct every request, decision and approval in the session after the fact.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 19.
