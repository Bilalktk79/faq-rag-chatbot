import faiss
import json
import numpy as np
import os
from .embedder import get_embedding


class VectorStore:
    def __init__(self, path=None):
        if path is None:
            # ✅ go to project root (faq-rag-chatbot)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
            path = os.path.join(BASE_DIR, "data", "faqs.json")

        print("📂 Loading FAQs from:", path)  # debug print

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.questions = [item["question"] for item in data]
        self.answers = [item["answer"] for item in data]

        embeddings = [get_embedding(q) for q in self.questions]
        self.embeddings = np.array(embeddings).astype("float32")

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def search(self, query, k=3):
        q_vec = np.array([get_embedding(query)]).astype("float32")

        distances, indices = self.index.search(q_vec, k)

        results = []
        for i, idx in enumerate(indices[0]):
            results.append({
                "question": self.questions[idx],
                "answer": self.answers[idx],
                "score": float(distances[0][i])
            })

        return results