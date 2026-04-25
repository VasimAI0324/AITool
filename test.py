from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Conversation history — yahan saari baatein store hongi
history = [
    {
        "role": "system",
        "content": "Tu ek helpful assistant hai jo Hinglish mein baat karta hai."
    }
]

print("AI Chatbot ready! 'quit' likho band karne ke liye\n")

# Infinite loop — jab tak quit na karo
while True:
    # User ka input lo
    user_input = input("Tu: ")
    
    # Quit check karo
    if user_input.lower() == "quit":
        print("Bye bhai!")
        break
    
    # User message history mein add karo
    history.append({
        "role": "user",
        "content": user_input
    })
    
    # AI se response lo — poori history bhejo
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )
    
    # AI ka jawab nikalo
    ai_reply = response.choices[0].message.content
    
    # AI reply bhi history mein add karo
    history.append({
        "role": "assistant",
        "content": ai_reply
    })
    
    print(f"AI: {ai_reply}\n")