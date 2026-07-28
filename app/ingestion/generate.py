from groq import Groq
import os
from app.ingestion.prompt import generate_text

client = Groq(
    api_key=os.getenv("API_KEY")
)

def generate_answer(question, chunks):

    prompt = generate_text(question, chunks)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Answer ONLY from the provided context. If the context doesn't contain the answer, say 'I don't know.'"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.0,
        max_tokens=60
    )

    return response.choices[0].message.content.strip()