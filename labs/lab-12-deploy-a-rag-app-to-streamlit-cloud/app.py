"""
Lab 12 — Deploy a RAG App to Streamlit Cloud

Take the RAG application from localhost to a public URL on Streamlit Community Cloud: pin the dependencies, push to GitHub, connect the repository, and inject API keys through the Secrets manager rather than committing them — the deployment pattern behind the course demo app.

Deliverable: A publicly reachable Streamlit Cloud URL running YOUR RAG app, with secrets configured and no keys in the repository.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Confirm requirements.txt lists every import your app makes — a missing line is the number-one deployment failure.

    # Step 2. Confirm .env is git-ignored and no key is in any tracked file.

    # Step 3. Commit and push your app to a PUBLIC GitHub repository.

    # Step 4. Go to https://share.streamlit.io, sign in with GitHub and click 'Create app' → 'Deploy a public app from GitHub'.

    # Step 5. Select your repository and branch, and set the main file path to app.py.

    # Step 6. Open 'Advanced settings' → 'Secrets' and paste your keys in TOML format — this is the production equivalent of .env.
    # OPENAI_API_KEY = "sk-..."
    # TAVILY_API_KEY = "tvly-..."

    # Step 7. Click Deploy and watch the build log install your dependencies.

    # Step 8. Open the public URL, upload an invoice and ask a question to confirm the deployed app really works.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
