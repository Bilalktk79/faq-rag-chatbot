def build_prompt(query, context):
    return f"""
You are a helpful AI assistant.

Use the following FAQ context to answer:

{context}

User Question: {query}

Answer clearly and professionally:
"""