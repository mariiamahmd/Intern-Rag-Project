from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import CrossEncoder

app = FastAPI()

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-12-v2"
)

class RerankRequest(BaseModel):
    question: str
    candidates: list[str]

@app.get("/")
def checkWorking():
    return{"Api is running"}

@app.post("/rerank")
def rerank(request: RerankRequest):

    pairs = [
        [request.question, candidate]
        for candidate in request.candidates
    ]

    scores = model.predict(pairs)

    return {
        "scores": scores.tolist()
    }