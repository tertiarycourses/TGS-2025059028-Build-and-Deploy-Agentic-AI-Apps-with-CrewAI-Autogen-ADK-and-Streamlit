# Lab 12 — Deploy a RAG App to Streamlit Cloud

**Learning outcome:** LO2 — Develop and deploy Agentic AI and RAG applications for inference on Streamlit Cloud
**Suggested duration:** 75 minutes

## Goal

Take the RAG application from localhost to a public URL on Streamlit Community Cloud: pin the dependencies, push to GitHub, connect the repository, and inject API keys through the Secrets manager rather than committing them — the deployment pattern behind the course demo app.

## What you'll build

A publicly reachable Streamlit Cloud URL running YOUR RAG app, with secrets configured and no keys in the repository.

**Tools:** Streamlit Community Cloud, GitHub, requirements.txt, Streamlit Secrets

## Workflow

1. Pin requirements.txt
2. Push to a public GitHub repo
3. Connect Streamlit Cloud to the repo
4. Add keys in Secrets (TOML)
5. Deploy and open the public URL

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Confirm requirements.txt lists every import your app makes — a missing line is the number-one deployment failure.

   ```bash
   cat requirements.txt
   ```

2. Confirm .env is git-ignored and no key is in any tracked file.

   ```bash
   git grep -nE 'sk-[A-Za-z0-9]{20}' || echo 'no keys committed - good'
   ```

3. Commit and push your app to a PUBLIC GitHub repository.

   ```bash
   git add -A && git commit -m 'Deploy RAG app' && git push origin main
   ```

4. Go to https://share.streamlit.io, sign in with GitHub and click 'Create app' → 'Deploy a public app from GitHub'.

5. Select your repository and branch, and set the main file path to app.py.

6. Open 'Advanced settings' → 'Secrets' and paste your keys in TOML format — this is the production equivalent of .env.

   ```bash
   OPENAI_API_KEY = "sk-..."
   TAVILY_API_KEY = "tvly-..."
   ```

7. Click Deploy and watch the build log install your dependencies.

8. Open the public URL, upload an invoice and ask a question to confirm the deployed app really works.

## Test it

Your app answers a question correctly at its public *.streamlit.app URL from a browser where you are NOT logged in, and the GitHub repository contains no API key anywhere.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 12.
