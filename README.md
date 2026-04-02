#  FAQ RAG Chatbot (CLI-based)

##  Features
- RAG (Retrieval-Augmented Generation)
- FAISS vector search
- FastAPI backend
- CLI chatbot interface
- LLM fallback for general queries

##  Tech Stack
- Python
- FastAPI
- FAISS
- HuggingFace API

##  How to Run

### Backend
```bash
cd backend
uvicorn app.main:app --reload
