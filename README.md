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

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mariiamahmd/Intern-Rag-Project.git
cd Intern-Rag-Project
```

### Install Dependencies

Install the required packages for both services:

```bash
pip install -r app/searchAPI/requirements.txt
pip install -r app/rerankerAPI/requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root and add:

```env
QDRANT_HOST=localhost
QDRANT_PORT=6333

API_KEY=your_groq_api_key

RERANKER_URL=http://127.0.0.1:8001/rerank

TOP_N=30
TOP_K=3
```

---

## Running the Project

### Option 1: Using Docker (Recommended)

Start all services (Qdrant, Search API, and Reranker API):

```bash
docker compose up -d
```

---

### Option 2: Running Locally

#### Step 1: Start Qdrant

Qdrant must be running before starting the APIs.

If you don't have Qdrant installed locally, start it using Docker:

```bash
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
```

#### Step 2: Start the Reranker API

Open a terminal and run:

```bash
cd app/rerankerAPI
uvicorn app:app --reload --port 8001
```

#### Step 3: Start the Search API

Open a second terminal and run:

```bash
cd app/searchAPI
uvicorn app:app --reload --port 8000
```

The APIs will be available at:

- Search API: `http://127.0.0.1:8000/docs`
- Reranker API: `http://127.0.0.1:8001/docs`