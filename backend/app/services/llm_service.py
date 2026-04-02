import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}


def query_llm(prompt):
    try:
        response = requests.post(
            HF_API,
            headers=HEADERS,
            json={"inputs": prompt},
            timeout=30
        )

        # ✅ RAW RESPONSE DEBUG
        print("🔍 RAW TEXT:", response.text)

        # ✅ EMPTY RESPONSE HANDLE
        if not response.text.strip():
            return "⚠️ Empty response from LLM (try again)"

        # ✅ SAFE JSON PARSE
        try:
            data = response.json()
        except:
            return f"⚠️ Non-JSON response:\n{response.text}"

        print("🔍 JSON:", data)

        # ✅ flan-t5 format
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]

        # ✅ error response
        if isinstance(data, dict) and "error" in data:
            return f"⚠️ LLM Error: {data['error']}"

        return "⚠️ Unknown response format"

    except Exception as e:
        return f"⚠️ Exception: {str(e)}"