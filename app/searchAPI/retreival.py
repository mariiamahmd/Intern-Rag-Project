from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2") # use the same model as for the data



client = QdrantClient(
    host=os.getenv("QDRANT_HOST"),
    port=int(os.getenv("QDRANT_PORT"))
)

# get user input
def retrieve(question):
    query_vector = model.encode(question).tolist()

# find vectors the are similar to this vector and return the top 30
    results = client.query_points(
        collection_name="purchase_orders",
        query=query_vector,
        limit=int(os.getenv("TOP_N"))
    ).points

#return them as a list not points
    output = []

    for result in results:
     output.append({
        "id": result.id,
        "score": result.score,
        "text": result.payload["text"]
    })


    return output
