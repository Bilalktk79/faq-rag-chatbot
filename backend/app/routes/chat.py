from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.rag_pipeline import get_context
from app.services.llm_service import query_llm
from app.utils.prompt import build_prompt

router = APIRouter()

class Query(BaseModel):
    message: str


@router.post("/chat")
def chat(q: Query):
    user_query = q.message

    # ✅ Step 1: RAG context
    context = get_context(user_query)

    # ✅ Step 2: Extract best answer from RAG
    try:
        top_answer = context.split("A:")[1].strip().split("\n")[0]
    except:
        top_answer = "Sorry, I couldn't find a relevant answer."

    # ✅ Step 3: Build prompt for LLM
    prompt = build_prompt(user_query, context)

    # ✅ Step 4: Call LLM
    llm_response = query_llm(prompt)

    # ✅ Step 5: Fallback system (VERY IMPORTANT)
    if (
        llm_response is None
        or "⚠️" in llm_response
        or "error" in llm_response.lower()
    ):
        return {
            "response": top_answer,
            "source": "RAG (fallback)"
        }

    # ✅ Step 6: Clean LLM output (optional polish)
    clean_response = llm_response.replace(prompt, "").strip()

    return {
        "response": clean_response,
        "source": "LLM + RAG"
    }