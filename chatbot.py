from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("Groq_API_KEY")
client = Groq(api_key = api_key)
while True:
    user_input = input("You: ")
    if not user_input:
        continue
    if user_input in ["exit", "quit", "bye", "thats all", "see you later", "stop"]:
        break
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    print(f"Bot: {response.choices[0].message.content}")
