from fastapi import FastAPI
from pydantic import BaseModel
from app.searchAPI.retreival import retrieve
from app.ingestion.generate import generate_answer
import httpx
import os
from dotenv import load_dotenv

load_dotenv()



app = FastAPI()

class SearchRequest(BaseModel):
    question: str

@app.get("/")
def checkWorking():
    return{"Api is running"}

@app.post("/search")
def search(request: SearchRequest):

    results= retrieve(request.question)
      # Get the text of each chunk
    candidates = [result["text"] for result in results]


    # Call the reranker and pass the parameters 
    response = httpx.post(
    os.getenv("RERANKER_URL"),
    json={
        "question": request.question,
        "candidates": candidates
    }
)

    scores = response.json()["scores"]

    # Pair each result with its reranker score
    reranked = list(zip(results, scores))

    # Sort by reranker score
    reranked.sort(
        key=lambda x: x[1],
        reverse=True
    )
    TOP_K = int(os.getenv("TOP_K"))

    top_chunks = [chunk for chunk, score in reranked[:TOP_K]]
    # Generate answer
    answer = generate_answer(
        request.question,
        top_chunks
    )
    return {
    "Question": request.question,
    "Answer": answer,
    "Sources": [
        {
            "id": chunk["id"]
        }
        for chunk in top_chunks
    ]
}
    
    