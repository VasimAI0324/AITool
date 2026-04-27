from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# App ka title
st.title("🤖 Mera AI Assistant")
st.caption("Powered by Groq + Llama")

# History initialize karo — sirf ek baar
if "history" not in st.session_state:
    st.session_state.history = [
        {
            "role": "system",
            "content": "Tu ek helpful assistant hai jo Hinglish mein baat karta hai."
        }
    ]

# Purani baatein display karo
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# User input lo
user_input = st.chat_input("Apna sawaal likho...")

if user_input:
    # User message dikhao
    st.chat_message("user").write(user_input)
    
    # History mein add karo
    st.session_state.history.append({
        "role": "user",
        "content": user_input
    })
    
    # AI se response lo
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.history
    )
    
    ai_reply = response.choices[0].message.content
    
    # AI reply dikhao
    st.chat_message("assistant").write(ai_reply)
    
    # History mein add karo
    st.session_state.history.append({
        "role": "assistant",
        "content": ai_reply
    })