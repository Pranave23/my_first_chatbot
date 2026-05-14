from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("Groq_API_KEY")
client = Groq(api_key = api_key)
conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]
while True:
    user_input = input("You: ")
    
    if not user_input:
        continue
    if user_input in ["exit", "quit", "bye", "thats all", "see you later", "stop"]:
        break
    conversation_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    print(f"Bot: {response.choices[0].message.content}")
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})      
    

