# Lab 20 — Deploy the Guardrailed Agentic AI App to Production

**Learning outcome:** LO3 — Deploy guardrails and model alignment techniques to ensure safe and aligned outputs
**Suggested duration:** 75 minutes

## Goal

Bring the whole course together: deploy the fully guardrailed multi-agent application to Streamlit Cloud with input guardrails, output filtering, human oversight, audit logging and spend controls, then verify the deployed app resists the attacks from Activity 15.

## What you'll build

A publicly deployed, fully guardrailed Agentic AI application that passes a live red-team re-test.

**Tools:** Streamlit Community Cloud, GitHub, Streamlit Secrets, all prior activity code

## Workflow

1. Assemble all guardrails in one app
2. Push and deploy to Streamlit Cloud
3. Configure Secrets + spend caps
4. Re-run the Activity 15 attacks
5. Complete the go-live checklist

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Combine your work into one production app: the agents from LU1, the RAG pipeline from LU2, and every guardrail from LU3.

2. Verify no secret is committed anywhere before you push.

   ```bash
   git grep -nE '(sk-|tvly-)[A-Za-z0-9]{20}' || echo 'clean'
   ```

3. Push to GitHub and deploy on Streamlit Cloud using the Activity 12 procedure.

   ```bash
   git add -A && git commit -m 'Guardrailed production app' && git push origin main
   ```

4. Add every required key in Streamlit Secrets and set a hard spend limit at the provider.

5. Re-run every attack from data/redteam_log.csv against the LIVE public URL — not localhost.

6. Confirm the audit log records the blocked attempts, and check the Streamlit Cloud logs for errors.

7. Complete the go-live checklist: secrets managed, input guardrails, output filtering, human oversight, audit logging, spend cap, error handling.

8. Share your public URL with a classmate and have them try to break it.

## Test it

Every attack that succeeded against the baseline in Activity 15 is blocked on the LIVE public URL, legitimate questions still work, and your go-live checklist is complete with all seven controls in place.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 20.
