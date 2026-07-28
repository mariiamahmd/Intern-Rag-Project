# RAG Purchase Order Assistant

An Advanced Retrieval-Augmented Generation (RAG) system that answers natural language questions about a purchase order CSV dataset.

The system uses a **two-stage retrieval pipeline**:
1. **Semantic Search** retrieves the most relevant purchase order records from Qdrant using vector embeddings.
2. **CrossEncoder Reranking** reorders the retrieved results to select the most relevant context before sending it to the LLM.

The language model is instructed to answer **only from the retrieved context**. If the answer is not found in the dataset, it responds with **"I don't know."** instead of generating unsupported information.

## Features

- CSV data cleaning and preprocessing
- Row-to-text conversion for embedding generation
- Semantic search with SentenceTransformers
- Qdrant vector database
- CrossEncoder reranking
- Grounded answer generation using an LLM
- Source citations returned with every answer
- FastAPI-based APIs
- Dockerized services for the API, reranker, and Qdrant

## Installation

```bash
git clone https://github.com/mariiamahmd/Intern-Rag-Project.git
cd Intern-Rag-Project
```

Install the required packages:

```bash
pip install -r app/searchAPI/requirements.txt
pip install -r app/rerankerAPI/requirements.txt
```

Run the project:

```bash
docker compose up -d
```
