"""
Lab 13 — Diagnose Deployment Failures from Error Logs

Deployments fail in a small number of predictable ways. Deliberately trigger the four most common failures, read the actual log output each produces, and build a reusable symptom → root-cause → fix table for diagnosing Agentic AI pipelines.

Deliverable: A completed error-log triage table mapping four real log signatures to their root causes and fixes.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Remove one package from requirements.txt, redeploy, and read the log. Record the exact first error line.

    # Step 2. Restore the package. Now delete one key from Streamlit Secrets, reboot the app and read the new error.

    # Step 3. Note the crucial difference: a missing dependency fails at BUILD time; a missing secret fails at RUN time.

    # Step 4. Trigger a rate-limit by sending many rapid requests, and observe the 429 response and its retry guidance.

    # Step 5. Break a @function_tool by removing its type hint, and read the resulting schema-validation error.
    # def tavily_search(query) -> str:   # type hint deliberately removed

    # Step 6. For each failure record the log signature, root cause, fix and prevention in data/error_triage.csv.

    # Step 7. Add structured logging so future failures are traceable rather than mysterious.
    # import logging; logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
