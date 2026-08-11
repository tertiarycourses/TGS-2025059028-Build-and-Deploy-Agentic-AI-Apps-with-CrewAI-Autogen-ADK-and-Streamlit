"""
Lab 18 — Evaluate Model Alignment — Helpful, Harmless, Honest

Alignment is trained into the model; guardrails are added by you. Build a small evaluation suite that scores your agent on helpfulness, harmlessness and honesty, and measure how RLHF-style alignment and your runtime guardrails contribute differently to the result.

Deliverable: A scored alignment evaluation across ten prompts, with the helpful/harmless/honest profile of your agent.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Write ten prompts spanning four categories: benign, grounded-factual, unknowable, and adversarial.

    # Step 2. Define your scoring rubric before you look at any output — 1 to 5 on each of helpful, harmless and honest.

    # Step 3. Run all ten prompts against the UN-guarded agent and score every response.

    # Step 4. Pay special attention to the 'unknowable' prompts: an honest agent says it does not know rather than inventing an answer.

    # Step 5. Run the same ten prompts against your GUARDED agent from Activities 16 and 17 and score again.

    # Step 6. Compare the two profiles and record where the guardrails helped — and where they cost helpfulness.

    # Step 7. Write one sentence distinguishing what alignment training fixed from what your runtime guardrails fixed.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
