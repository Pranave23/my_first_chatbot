import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("Groq_API_KEY")
client = Groq(api_key = api_key)
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        {"role": "system", "content": "You're a helpful assistant."}
    ]
st.title("ChatBot")
for message in st.session_state.conversation_history:
    if message["role"] != "system": #if the message is not the system message, then it can be dispalyed, usewr dont need to see the system message 
        with st.chat_message(message["role"]):
            st.write(message["content"])
user_input = st.chat_input("Enter your message here...")
if user_input:
    st.session_state.conversation_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=st.session_state.conversation_history)
    with st.chat_message("assistant"):
       st.write(f"{response.choices[0].message.content}")
    st.session_state.conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})