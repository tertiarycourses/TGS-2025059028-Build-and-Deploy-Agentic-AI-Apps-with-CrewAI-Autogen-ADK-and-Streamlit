"""
Lab 2 — Compare CrewAI, AutoGen and the OpenAI Agents SDK

Before writing agent code, decide which framework fits a given problem. Score all three frameworks against a real requirement set — orchestration style, human-in-the-loop, tool ecosystem, learning curve and production readiness — and justify a recommendation.

Deliverable: A completed framework-comparison matrix with a written, evidence-based recommendation for one named use case.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Write down a concrete use case in one sentence, e.g. 'automate customer-support triage for a SaaS product'.

    # Step 2. List your hard requirements: does it need human approval? multi-model? streaming? a specific cloud?

    # Step 3. Open data/framework_matrix.csv and score each framework 1–5 against every criterion for YOUR use case.

    # Step 4. Multiply each score by the criterion weight and total each framework's column.

    # Step 5. Note where the top two frameworks differ most — that difference is usually the real deciding factor.

    # Step 6. Write a three-sentence recommendation: the framework, the deciding criterion, and the main risk you accept.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
