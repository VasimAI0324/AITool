from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "Tu ek helpful teacher hai jo sirf Hinglish mein padhata hai. Har jawab simple aur short deta hai."
        },
        {
            "role": "user", 
            "content": "Photosynthesis kya hai?"
        }
    ]
)

print(response.choices[0].message.content)