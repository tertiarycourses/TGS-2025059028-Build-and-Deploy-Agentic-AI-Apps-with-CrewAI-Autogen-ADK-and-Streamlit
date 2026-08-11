"""
Lab 19 — Add Human Oversight and an Audit Log

Automated guardrails cannot judge every case. Add a risk-based approval gate that routes high-impact or low-confidence actions to a human before execution, and write an audit log that records every guardrail decision for later review.

Deliverable: An agent with a human-approval gate on high-risk actions and a persistent JSONL audit log of every decision.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. List the actions your agent can take and classify each as low, medium or high risk.

    # Step 2. Set the policy: low risk executes automatically, medium risk is logged, high risk requires explicit human approval.

    # Step 3. Implement the approval gate in Streamlit for high-risk actions.
    # if risk == 'high':
    #     st.warning(f'Approval required: {action}')
    #     if not st.button('Approve'): st.stop()

    # Step 4. Write every guardrail decision to an append-only audit log as one JSON object per line.
    # import json, datetime
    # with open('data/audit_log.jsonl','a') as f:
    #     f.write(json.dumps({'ts': datetime.datetime.now().isoformat(), 'prompt': p, 'decision': d, 'risk': risk}) + '\n')

    # Step 5. Include in each record what was requested, what the guardrail decided, the risk level and who approved it.

    # Step 6. Run a mixed session: several benign requests and two high-risk ones, approving one and rejecting the other.

    # Step 7. Read back the audit log and confirm you can reconstruct exactly what happened and why.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
