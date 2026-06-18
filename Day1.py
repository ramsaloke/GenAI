from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   "role": "system",
            "content": """ You are senior backend engineer explain concepts simply only give answers 
            that related to javascript ecosystem like expressjs , nodejs , nest js etc.. if user asks 
            other than js ecosystem simply say im sorry

"""
        },
        {
            "role": "user",
            "content": "what is python can you explain me"
        }
    ]
)

print(response.choices[0].message.content)