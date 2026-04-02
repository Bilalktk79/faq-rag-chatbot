from app.rag.vector_store import VectorStore

store = VectorStore()

def get_context(query):
    results = store.search(query, k=1)

    best = results[0]

    # 🔥 CONFIDENCE CHECK
    if best["score"] > 1.5:   # threshold (tune kar sakte ho)
        return None

    return f"Q: {best['question']}\nA: {best['answer']}"