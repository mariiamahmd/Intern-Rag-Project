def generate_text(question, retrieved_chunks, top_k=3):

    contexts = []

    for chunk in retrieved_chunks[:top_k]:

        section = f"""
Purchase Order Information

{chunk["text"]}
"""

        metadata = []

        for key, value in chunk.items():
            if key != "text":
                metadata.append(f"{key}: {value}")

        if metadata:
            section += "\n\nDetails:\n"
            section += "\n".join(metadata)

        contexts.append(section.strip())

    context = "\n\n-----------------------------\n\n".join(contexts)

    prompt = f"""
You are a helpful assistant answering questions about purchase orders.

Answer ONLY using the information provided below.

Rules:
- Use only the provided information.
- Do not use outside knowledge.
- Do not repeat or quote the context.
- Answer naturally, as if speaking to a user.
- If multiple purchase orders match, list them clearly.
- If the answer is not present, reply exactly:
I don't know.

Purchase Orders:
{context}

Question:
{question}

Answer:
"""

    return prompt

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