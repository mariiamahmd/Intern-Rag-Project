from app.ingestion.preprocessing import clean_data
from app.ingestion.text_builder import row_to_text

from sentence_transformers import SentenceTransformer
from qdrant_client import models, QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)

COLLECTION_NAME = "purchase_orders"


def ingest():

    # Load model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Connect to Qdrant
    client = QdrantClient(
        host="localhost",
        port=6333 #qdrant at port 6333
    )

    print(client.get_collections())#send existing collections

    # Create collection if it doesn't exist
    collections = client.get_collections().collections

    if COLLECTION_NAME not in [c.name for c in collections]:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384, #each embed vector has 384 dimensions bec model outputs this size
                distance=Distance.COSINE # cosine distance for similarity
            )
        )

    # Load and clean data
    
    df = clean_data()


    points = []

#loop through each row
    for index, row in df.iterrows():

      text = row_to_text(row)

      metadata = {
    "row_number": index,
    "po_no": row["po_no"],
    "line_num": row["line_num"],
    "creation_date": str(row["creation_date"]),
    "approve_date": str(row["approve_date"]),
    "closed_date": str(row["closed_date"]),
    "main_category": row["main_category"],
    "group_category": row["group_category"],
    "sub_group_category": row["sub_group_category"],
    "vendor_no": row["vendor_no"],
    "vendor_site_code": row["vendor_site_code"]
}

# =============To print the first 5 chunks (add .head(5)in the for loop)================
    #   print("=" * 80)
    #   print(f"Chunk {index + 1}")
    #   print("=" * 80)
    #   print(text)

    #   print("\nMetadata:")
    #   for key, value in metadata.items():
    #     print(f"{key}: {value}")

    #   print("\n")
     


      
      embedding = model.encode(text).tolist() # convert text to embeddings
      
      payload = {
    "text": text,
    **metadata
}
# pointstruct==>one record in the collection has the id embedding vector and text with its meta data
      points.append(
    PointStruct(
        id=index,
        vector=embedding,
        payload=payload
    )
)
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"{len(points)} chunks uploaded successfully.")


if __name__ == "__main__":
    ingest()




