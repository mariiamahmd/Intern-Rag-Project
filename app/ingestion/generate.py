from transformers import pipeline
from app.ingestion.prompt import generate_text

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

def generate_answer(question, chunks):

    prompt = generate_text(question, chunks)

    messages = [
        {
            "role": "system",
            "content": "Answer ONLY from the provided context. If the context doesn't contain the answer, say 'I don't know.'"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = generator(
    prompt,
    max_new_tokens=60,
    do_sample=False,
    temperature=0.0,
    return_full_text=False
)

    return response[0]["generated_text"].strip()