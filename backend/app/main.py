from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router

app = FastAPI(title="FAQ RAG Chatbot")

# CORS (frontend connect ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes include
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "FAQ RAG Chatbot running 🚀"}