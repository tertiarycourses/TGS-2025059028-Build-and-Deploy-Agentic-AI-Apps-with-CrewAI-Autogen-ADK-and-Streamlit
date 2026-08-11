"""
Lab 20 — Deploy the Guardrailed Agentic AI App to Production

Bring the whole course together: deploy the fully guardrailed multi-agent application to Streamlit Cloud with input guardrails, output filtering, human oversight, audit logging and spend controls, then verify the deployed app resists the attacks from Activity 15.

Deliverable: A publicly deployed, fully guardrailed Agentic AI application that passes a live red-team re-test.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Combine your work into one production app: the agents from LU1, the RAG pipeline from LU2, and every guardrail from LU3.

    # Step 2. Verify no secret is committed anywhere before you push.

    # Step 3. Push to GitHub and deploy on Streamlit Cloud using the Activity 12 procedure.

    # Step 4. Add every required key in Streamlit Secrets and set a hard spend limit at the provider.

    # Step 5. Re-run every attack from data/redteam_log.csv against the LIVE public URL — not localhost.

    # Step 6. Confirm the audit log records the blocked attempts, and check the Streamlit Cloud logs for errors.

    # Step 7. Complete the go-live checklist: secrets managed, input guardrails, output filtering, human oversight, audit logging, spend cap, error handling.

    # Step 8. Share your public URL with a classmate and have them try to break it.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
