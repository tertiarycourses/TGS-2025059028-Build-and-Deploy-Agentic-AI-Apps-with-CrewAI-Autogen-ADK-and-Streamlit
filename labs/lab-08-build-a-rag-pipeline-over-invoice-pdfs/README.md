# Lab 8 — Build a RAG Pipeline over Invoice PDFs

**Learning outcome:** LO2 — Develop and deploy Agentic AI and RAG applications for inference on Streamlit Cloud
**Suggested duration:** 75 minutes

## Goal

Build the full Retrieval-Augmented Generation pipeline end to end: extract text from invoice PDFs, chunk it with overlap, embed the chunks, store them in ChromaDB, and answer natural-language questions grounded in the retrieved context. This is labs/lab-08-build-a-rag-pipeline-over-invoice-pdfs/app.py.

## What you'll build

A Streamlit app that indexes the sample invoice PDFs and answers questions about them with grounded, cited answers.

**Tools:** OpenAI Embeddings, ChromaDB, pypdf, Streamlit, labs/lab-08-build-a-rag-pipeline-over-invoice-pdfs/app.py, data/invoices/

## Workflow

1. Extract PDF text with pypdf
2. Chunk with 120-char overlap
3. Embed and store in ChromaDB
4. Retrieve top-k by similarity
5. Augment the prompt and answer

## Setup

```bash
# from this lab folder
pip install -r requirements.txt
cp ../.env.example ../.env      # then paste in your own keys
```

## Step-by-step

1. Open labs/lab-08-build-a-rag-pipeline-over-invoice-pdfs/app.py and find load_pdf_text() — pypdf extracts text page by page.

2. Find chunk_text() and note the two parameters that govern retrieval quality: chunk_size=800 and overlap=120.

3. Understand WHY chunks overlap: without it, a sentence split across a boundary is retrievable from neither chunk.

4. Find index_pdf() — it embeds each chunk with text-embedding-3-large and adds it to the ChromaDB collection.

5. Run the app and upload several PDFs from the 'data/invoices' folder.

   ```bash
   streamlit run app.py
   ```

6. Ask a question that requires retrieval, e.g. 'What is the total on Aaron Hawkins' invoice 47905?'

7. Ask about an invoice you did NOT upload and confirm the app says it cannot find it — grounding working correctly.

8. Change chunk_size to 300, re-index, and compare answer quality to judge the chunking trade-off yourself.

## Test it

The app answers correctly for uploaded invoices AND declines to answer about a document that was never indexed — demonstrating that answers come from retrieved context, not model hallucination.

---

Part of **Build and Deploy Agentic AI Apps with CrewAI, Autogen, ADK and Streamlit** (TGS-2025059028) — Tertiary Infotech Academy Pte Ltd. Full step-by-step detail is in the Learner Guide, Activity 8.
