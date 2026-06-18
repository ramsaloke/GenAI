import json

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

user_input = input("Tell me your problem: ")

prompt = f"""
You are a confidence coach.

Analyze the user's message.

Return ONLY a raw JSON object.

Do not use markdown.
Do not use ```json.
Do not add explanations.

{{
  "problem": "",
  "confidence_score": 0,
  "advice": "",
  "daily_exercise": ""
}}

User:
{user_input}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

result = json.loads(
    response.choices[0].message.content
)

print("\n=== Confidence Analysis ===")
print("Problem:", result["problem"])
print("Confidence Score:", result["confidence_score"])
print("Advice:", result["advice"])
print("Daily Exercise:", result["daily_exercise"])
