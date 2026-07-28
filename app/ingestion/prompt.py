def generate_text(question, retrieved_chunks, top_k=3):

    context = ""

    for i, chunk in enumerate(retrieved_chunks[:top_k], start=1):

        context += f"Context {i}\n"
        context += f"Text:\n{chunk['text']}\n\n"

        context += "Metadata:\n"

        for key, value in chunk.items():
            if key != "text":
                context += f"- {key}: {value}\n"

        context += "\n" + "=" * 60 + "\n\n"

    prompt = f"""
You are a helpful assistant answering questions about purchase orders.

Answer ONLY using the information provided in the context below.

Rules:
- Do NOT use outside knowledge.
- Do NOT make up information.
- If the answer is not found in the context, reply exactly:
I don't know.
- Give a short, direct answer.
- Do NOT repeat the context.
- If multiple purchase orders match, list them clearly.

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt