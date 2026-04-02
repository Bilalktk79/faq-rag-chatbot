import requests

API_URL = "http://127.0.0.1:8000/chat"

def chat():
    print("\n🧠 AI Assistant Ready (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        try:
            response = requests.post(
                API_URL,
                json={"message": user_input}
            )

            data = response.json()
            print(f"AI: {data['response']}\n")

        except Exception as e:
            print("⚠️ Error:", e)


if __name__ == "__main__":
    chat()