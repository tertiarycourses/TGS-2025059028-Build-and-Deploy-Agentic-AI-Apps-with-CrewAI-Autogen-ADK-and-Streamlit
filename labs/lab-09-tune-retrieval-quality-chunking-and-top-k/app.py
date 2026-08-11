"""
Lab 9 — Tune Retrieval Quality — Chunking and Top-K

Retrieval quality decides answer quality. Run a controlled experiment across chunk sizes and top-k values on the same question set, record which configuration retrieves the right context, and choose settings you can defend with evidence.

Deliverable: A completed retrieval-tuning table showing accuracy at three chunk sizes and three top-k values, with a chosen configuration.
"""

from dotenv import load_dotenv

load_dotenv()


def main():
    # Step 1. Write five questions whose correct answers you can verify by opening the PDFs yourself — these are your gold standard.

    # Step 2. Set chunk_size=300 and overlap=50, restart the app, re-index and run all five questions. Record hit or miss.

    # Step 3. Repeat with chunk_size=800 / overlap=120, then chunk_size=1500 / overlap=200.

    # Step 4. Now hold chunk size at the best value and vary the retrieval depth in collection.query().
    # results = collection.query(query_texts=[question], n_results=3)   # try 1, 3, then 5

    # Step 5. Record every result in data/retrieval_tuning.csv as you go — do not rely on memory.

    # Step 6. Note the failure mode at each extreme: tiny chunks lose context, huge chunks dilute the signal, high top-k adds noise.

    # Step 7. State your chosen chunk_size and top-k, and the specific evidence from your table that supports it.

    print("Work through the steps above — see README.md and the Learner Guide.")


if __name__ == "__main__":
    main()
